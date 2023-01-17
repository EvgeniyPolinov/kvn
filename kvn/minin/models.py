from decimal import Decimal

from django.conf import settings
from django.db import models
from django.urls import reverse


class Comand(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_evaluation = models.IntegerField(null=True,)
    second_appreciation = models.IntegerField(null=True)
    third_assessment = models.IntegerField(null=True)
    fourth_assessment = models.IntegerField(null=True)
    fifth_assessment = models.IntegerField(null=True)
    final_score = models.FloatField(null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)




    def save(self, *args, **kwargs):
        self.first_evaluation = int(self.first_evaluation)
        self.second_appreciation = int(self.second_appreciation)
        self.third_assessment = int(self.third_assessment)
        self.fourth_assessment = int(self.fourth_assessment)
        self.fifth_assessment = int(self.fifth_assessment)
        self.final_score = (self.first_evaluation + self.second_appreciation + self.third_assessment + self.fourth_assessment + self.fifth_assessment)/5
        super(Comand, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/juds'

    def get_absolute_url2(self):
        return f'/update/{self.pk}/'

    class Meta:
        ordering = ['-final_score']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Judj(models.Model):
    user_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    first_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.first_name


