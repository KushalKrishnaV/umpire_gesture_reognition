from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)