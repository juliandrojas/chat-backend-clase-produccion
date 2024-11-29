from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=100, unique=True
    )
    #Se va a cargar en un directorio
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True
    )
    file_updated = models.FileField(upload_to='files/', blank=True, null=True)
    
class Message(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )