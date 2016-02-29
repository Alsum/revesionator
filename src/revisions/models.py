from django.db import models
from articles.models import Article
from django.contrib.auth.models import User


class Revision(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.article.title + " " + "Revision"
