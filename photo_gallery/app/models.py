from django.db import models
import uuid

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    likes = models.PositiveIntegerField(default=0)

class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, default=uuid.uuid4)
