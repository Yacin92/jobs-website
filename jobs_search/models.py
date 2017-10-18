from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Annonce(models.Model):

    domaines_list = (('technology', 'technology'), ('mecanique', 'mecanique'))
    region_list = (('sfax', 'sfax'), ('monastir', 'monastir'))

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100, choices = domaines_list, default=1)
    region = models.CharField(max_length=100, choices = region_list, default=1)
    description = models.CharField(max_length=1500)
    image = models.FileField()
    date = models.DateField(auto_now=True)
    phone = models.CharField(max_length=100)


    def get_absolute_url(self):
        return reverse('jobs_search:index')


    def __str__(self):
        return self.title
