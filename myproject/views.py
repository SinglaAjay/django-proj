from django.http import JsonResponse
from django.shortcuts import render
import numpy as np

import pyodbc
import myproject.dbconfig as db_config

print("Available ODBC drivers:", pyodbc.drivers())
print(pyodbc.drivers())

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=singla-db-server.database.windows.net;"
    "UID=dbadmin;"
    "PWD=password@2k26$$;"
    "DATABASE=pyhon-learning;"
    "TrustServerCertificate=yes;"
)
cursor = conn.cursor()

print("Database connection established successfully.")

def contact(request):
    """Render an HTML response with context data."""
    print("Rendering contact page with context:")

    x=[1,2,3]
    y= np.array(x)
    print("x:", x)
    return render(request, "contact.html")

def render_json_response(data, status=200):
    """Render a JSON response."""
    return JsonResponse(data, status=status)

def  submit_contact(request):
    """Handle contact form submission."""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Received contact form submission: name={name}, email={email}")
        # Here you would typically process the form data, e.g., save it to a database or send an email
        response_data = {"message": "Contact form submitted successfully!"}

    cursor.execute(
        "INSERT INTO Users (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()

    print("Data inserted into database successfully.")
        
    return render(request, "contact.html")

def contact_json(request):
    """Render a JSON response with contact information."""
    print("Rendering contact JSON response")
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    return render_json_response(data)