from django.db import models

# Themes

class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField(blank=True)
