from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title
