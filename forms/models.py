from django.db import models

from django.db import models

class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    attachment = models.ImageField(upload_to='attachments/', blank=True, null=True)

  

