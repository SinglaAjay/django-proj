from django.http import JsonResponse
from django.shortcuts import render

def contact(request):
    """Render an HTML response with context data."""
    print("Rendering contact page with context:")
    return render(request, "contact.html")

def render_json_response(data, status=200):
    """Render a JSON response."""
    return JsonResponse(data, status=status)