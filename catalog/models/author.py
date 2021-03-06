# Imported from Django.
from django.db import models

# Imported from django_countries.
from django_countries.fields import CountryField
# https://pypi.org/project/django-countries/

# List of languages.
from .languaje import LANGUAGE_CHOICE


class Author(models.Model):
	first_name = models.CharField(
		max_length=64,
		null=False,
		blank=False,
	)
	last_name = models.CharField(
		max_length=64,
		null=True,
		blank=True,
	)
	Pseudonymous = models.CharField(
		max_length=64,
		null=True,
		blank=True,
	)
	date_of_birth = models.DateField(
		null=False,
		blank=False,
	)
	date_of_death = models.DateField(
		null=True,
		blank=True,
	)
	nationality = CountryField(
		blank_label='(select country)'
	)
	mother_tongue = models.CharField(
		choices=LANGUAGE_CHOICE,
		max_length=2,
		null=True,
		blank=True,
	)
	books = models.ManyToManyField(
		'Book',
		through='RelationshipBookAuthor'
	)
	
	# To Do: create a field 'genre'. It will be a ManyToMany field.
	
	class Meta:
		ordering = ['last_name', 'first_name']
	
	def __str__(self):
		return f'{self.last_name}, {self.first_name}'
