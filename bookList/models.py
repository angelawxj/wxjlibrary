from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images_url = models.CharField(max_length=200, default='DEFAULT VALUE')
    author = models.CharField(max_length=50, default='wxj')
	
    def __str__(self):
        return self.title
