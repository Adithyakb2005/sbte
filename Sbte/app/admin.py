from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Cart

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'added_on')
