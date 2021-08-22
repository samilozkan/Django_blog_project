from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishing_date = models.DateTimeField(verbose_name='Publishing Date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absoulute_url(self):
        return "/post/{}".format(self.id)