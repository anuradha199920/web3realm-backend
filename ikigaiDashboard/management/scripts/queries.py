from django.db import connection


def run_raw_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return results


def market_overview_query():
    print(run_raw_sql("SELECT * FROM market_overview"))