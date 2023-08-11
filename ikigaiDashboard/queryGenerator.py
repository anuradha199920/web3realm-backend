from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

openai_api_key = "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"


# You can provide a custom args schema to add descriptions or custom validation

chatOpenAi = ChatOpenAI(openai_api_key=openai_api_key)

context = """
    You are an intelligent sql query generator. You will be given a question or a statement regarding NFT Trades. You have to provide the correct query for the given ask.
table name: base_data

The base_data table is standard and will be fixed for all queries

The below list contains column name, data type and description of each column respectively in base_data :
1.block_time,	timestamp with time zone(UTC),	When was this trade executed
2.nft_token_id,	varchar,	The token_id that was traded (e.g. 235)
3.is_wash_trade, boolean,	true = wash trade , false = organic trade
4.aggregator_name,	varchar,	Was this trade made using an aggregator (Yes : Name of aggregator, No : Null)
5.amount_usd, numeric,	USD value of the trade at time of execution
6.seller, varbinary, Seller of NFTs
7.buyer, varbinary, Buyer of NFTs
8.currency_symbol, varchar, The Currency used for this trade
9.nft_contract_address, varbinary, The contract address of the NFT traded
10.tx_hash, varbinary, The hash of this transaction
11.block_number, integer, The block_number that this trade was done in
12.unique_trade_id, varchar, unique_id for each trade
13.amount_original, numeric, value of trade as per currency_symbol

1/ Keep in mind that NFTs can be traded on various platforms, including 'OpenSea', 'Blur', and others. To categorize trades by platform, utilize the following condition:: “CASE WHEN LENGTH(aggregator_name) > 1 THEN Lower(aggregator_name) ELSE Lower(project) END AS project” and then do group by project

2/ To remove wash trades use filter “is_wash_trade = false”

3/ An NFT is uniquely defined by combination of nft_contract_address and token_id
"""

example = """
Input = “what is the highest sale for yesterday”
Output = 

select max(amount_usd) as Highest_sale
from base_data 
where DATE_TRUNC('day', block_time) > DATE_TRUNC('day', NOW() - INTERVAL '1' day)
and is_wash_trade = false
group by 1
order by 2 desc

Input = “find number of daily sales for past 1 week”
Output =
select DATE_TRUNC('day', block_time) as time, count(*) as sales from base_data 
where block_time >= date_trunc('day', NOW() - interval ‘7’ day)
group by 1"""
base_context =" context + example"


def get_query(user_input):
    template = context+example
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(
        llm=chatOpenAi,
        prompt=chat_prompt
    )
    return chain.run(user_input)


