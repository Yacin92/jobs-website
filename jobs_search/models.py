from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    STATUS = (
        ('employee', 'employee'),
        ('employer', 'employer')
    )
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.status)


class Annonce(models.Model):

    domaines_list = (('technology', 'technology'), ('mechanics', 'mechanics'), ('commerce', 'commerce')
        , ('training and education', 'training and education'), ('services', 'services'), ('tourism', 'tourism'))



    region_list = (('sfax', 'sfax'), ('monastir', 'monastir'), ('gafsa', 'gafsa'), ('tunis', 'tunis')
        , ('sousse', 'sousse'), ('gabes', 'gabes'), ('mahdia', 'mahdia'), ('beja', 'beja')
        , ('tataouine', 'tataouine'),)

    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
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

class Request(models.Model):
    annonce = models.ForeignKey(to=Annonce, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    employee_cv_file=models.FileField()

    def __str__(self):
        return "{} - {}".format(self.annonce.title, self.employee)