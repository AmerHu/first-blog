from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)
    published_date = models.TextField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
