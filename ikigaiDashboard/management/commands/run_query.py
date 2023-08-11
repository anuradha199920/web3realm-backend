from django.core.management.base import BaseCommand
from ikigaiDashboard.queryGenerator import get_query


class Command(BaseCommand):
    help = 'Run sql query and print the fetched information.'

    def handle(self, *args, **options):
        print(get_query("Number of trades yesterday that were sold in profit and loss respectively"))
