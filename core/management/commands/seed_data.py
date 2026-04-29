import csv
from django.core.management.base import BaseCommand
from core.models import Viewer, Account, Behavior

class Command(BaseCommand):
    help = "Load CSV data into database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["csv_file"]

        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)


            for row in reader:
                
                viewer = Viewer.objects.create(
                    age=row["age"],
                    gender=row["gender"],
                    country=row["country"],
                    primary_device=row["primary_device"],
                    devices_used=row["devices_used"],
                )
                account = Account.objects.create(
                    viewer=viewer,
                    account_age_months=row["account_age_months"],
                    subscription_type=row["subscription_type"],
                    monthly_fee=row["monthly_fee"],
                    payment_method=row["payment_method"],
                )
                
                Behavior.objects.create(
                    account=account,
                    favorite_genre=row["favorite_genre"],
                    avg_watch_time_mins=row["avg_watch_time_minutes"],
                    watch_sessions_per_week=row["watch_sessions_per_week"],
                    binge_watch_sessions=row["binge_watch_sessions"],
                    completion_rate=row["completion_rate"],
                    rating_given=row["rating_given"],
                    content_interactions=row["content_interactions"],
                    recommendation_click_rate=row["recommendation_click_rate"],
                    days_since_last_login=row["days_since_last_login"],
                    churned = row['churned'].strip().lower() == 'yes'
                )
                
                

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))