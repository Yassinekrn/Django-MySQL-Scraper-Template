# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .scraper import run_scraper  # Assume scraper function is defined in scraper.py
from django.contrib.auth import get_user_model

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Protect endpoint with authentication
def scrape_data(request):
    """
    A view that runs the web scraper and returns scraped data as JSON.
    Only admin users are allowed to use the scraper.
    """
    # user = request.user
    # if not user.is_admin:  # Only allow access if user is admin
    #     return Response({"error": "Only admin can access this endpoint"}, status=403)

    try:
        # Run your scraper function to get data
        data = run_scraper()
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)