from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Annonce(models.Model):

    domaines_list = (('technology', 'technology'), ('mechanics', 'mechanics'), ('commerce', 'commerce')
        , ('training and education', 'training and education'), ('services', 'services'), ('tourism', 'tourism'))



    region_list = (('sfax', 'sfax'), ('monastir', 'monastir'), ('gafsa', 'gafsa'), ('tunis', 'tunis')
        , ('sousse', 'sousse'), ('gabes', 'gabes'), ('mahdia', 'mahdia'), ('beja', 'beja')
        , ('tataouine', 'tataouine'),)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100, choices = domaines_list, default=1)
    region = models.CharField(max_length=100, choices = region_list, default=1)
    description = models.TextField(max_length=1500)
    image = models.FileField()
    date = models.DateField(auto_now=True)
    phone = models.PositiveIntegerField()


    def get_absolute_url(self):
        return reverse('jobs_search:index')


    def __str__(self):
        return self.title
