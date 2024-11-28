from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Home Page View
def home_view(request):
    courses = Course.objects.all()  # Fetch all available courses
    return render(request, 'home.html', {'courses': courses})

# About Us Page View
def about_view(request):
    return render(request, 'about.html')

# All Courses Page View
def courses_view(request):
    courses = Course.objects.all()  
    return render(request, 'courses.html', {'courses': courses})

# Course Detail View
def course_detail_view(request, id):
    # Try to fetch the course object by its ID
    course = Course.objects.filter(id=id).first()
    
    if not course:
        # If no course is found, you can set a message or render a different page
        return render(request, 'course_not_found.html')  # Or pass a custom message to the template
    
    # If the course is found, render the course details template
    return render(request, 'course_detail.html', {'course': course})

# Placements Page View
def placements_view(request):
    return render(request, 'placements.html')

# Contact Us Page View
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                f'Contact Us Message from {name}',
                message,
                email,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_thank_you')
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}", status=500)

    return render(request, 'contact.html')

# Thank You Page for Contact Form
def contact_thank_you(request):
    return render(request, 'contact_thank_you.html')

# Register Page View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Authenticate and log the user in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 

    return render(request, 'register.html')
