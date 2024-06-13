from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date_published = models.DateField()

    def __str__(self):
        return self.title
