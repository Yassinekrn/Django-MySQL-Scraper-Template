# scraper/urls.py

from django.urls import path
from .views import scrape_data

urlpatterns = [
    path('scrape/', scrape_data),  # Route to trigger the web scraper
]
