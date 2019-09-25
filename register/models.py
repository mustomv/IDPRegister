from django.db import models
from django.conf import settings
from django.utils import timezone
from django_countries.fields import CountryField


class Person(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	full_name = models.CharField(max_length=200, blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	id_card_no = models.CharField(max_length=50, blank=True, null=True)
	nationality = CountryField()
	passportno = models.CharField(max_length=50, blank=True, null=True)
	permanent_address = models.CharField(max_length=200, blank=True, null=True)
	current_address = models.CharField(max_length=200, blank=True, null=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.full_name