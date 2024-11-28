from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,),
    path('about/', views.about_view, name='about_view'), 
    path('courses/', views.courses_view, name='courses_view'), 
    path('courses/<int:id>/', views.course_detail_view, name='course_detail'),

    path('placements/', views.placements_view, name='placements_view'),  
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/thank-you/', views.contact_thank_you, name='contact_thank_you'), 
    path('register/', views.register_view, name='register'),  
]
