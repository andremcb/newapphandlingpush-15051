from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f'/api/v1/customtext/{self.id}/'

    @property
    def field(self):
        return 'title'


class HomePage(models.Model):
    body = models.TextField()
    content = models.TextField()
    name = models.CharField()
    tag = models.CharField()

    @property
    def api(self):
        return f'/api/v1/homepage/{self.id}/'

    @property
    def field(self):
        return self.body
