import requests
import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Movie

     
class Command(BaseCommand):
    def handle(self, *args, **options):
        API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNGU4ODkwOGUzNTQ1YWNjN2U3Mzg3ZTI3MTNmZDc3YiIsIm5iZiI6MTc3NzgyMDEzOC45MzEsInN1YiI6IjY5Zjc2MWVhYTM1YmY4MzAyOWQ1N2Y2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DksrcQuOaiAtsbLntQ2n4hBDB1_Az9ZubaJ39p8ksbQ"

        url = "https://api.themoviedb.org/3/trending/movie/week"

        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)

        data = response.json()['results']

        for row in data:
            movie = Movie.objects.create(
                title=row['title'],
                overview=row['overview'],
                image=row['poster_path'],
                popularity=row['popularity']
            )

        



