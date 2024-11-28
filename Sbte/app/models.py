from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.title
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link to the Course model
    added_on = models.DateTimeField(auto_now_add=True)  # Timestamp when added to cart

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"