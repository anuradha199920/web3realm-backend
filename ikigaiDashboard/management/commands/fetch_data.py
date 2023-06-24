from django.core.management.base import BaseCommand
from ikigaiDashboard.management.scripts.fetch_data_and_store import fetch_and_store_data

class Command(BaseCommand):
    help = 'Fetch data from the API and store it in the database'

    def handle(self, *args, **options):
        fetch_and_store_data()
