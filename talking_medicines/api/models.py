from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=255)
    author_flair_text = models.CharField(max_length=255, blank=True, null=True)
    author_flair_text_color = models.CharField(max_length=10, blank=True, null=True)
    body = models.TextField()
    id = models.CharField(max_length=255, primary_key=True)
    permalink = models.CharField(max_length=255)
    score = models.IntegerField()
    subreddit = models.CharField(max_length=255)

    def __str__(self):
        return self.id
