from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
	timestamp = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return str(self.id) + " - " + str(self.timestamp)

class Locus(models.Model):
	user_id = models.ForeignKey(User)
	timestamp = models.DateTimeField(default=datetime.now)

	OPTION = (
		('A', 'A'), 
		('B', 'B'),
		)

	question_1 = models.CharField(max_length=1, choices=OPTION)
	question_2 = models.CharField(max_length=1, choices=OPTION)
	question_3 = models.CharField(max_length=1, choices=OPTION)
	question_4 = models.CharField(max_length=1, choices=OPTION)
	question_5 = models.CharField(max_length=1, choices=OPTION)
	question_6 = models.CharField(max_length=1, choices=OPTION)
	question_7 = models.CharField(max_length=1, choices=OPTION)
	question_8 = models.CharField(max_length=1, choices=OPTION)
	question_9 = models.CharField(max_length=1, choices=OPTION)
	question_10 = models.CharField(max_length=1, choices=OPTION)
	
	question_11 = models.CharField(max_length=1, choices=OPTION)
	question_12 = models.CharField(max_length=1, choices=OPTION)
	question_13 = models.CharField(max_length=1, choices=OPTION)
	question_14 = models.CharField(max_length=1, choices=OPTION)
	question_15 = models.CharField(max_length=1, choices=OPTION)
	question_16 = models.CharField(max_length=1, choices=OPTION)
	question_17 = models.CharField(max_length=1, choices=OPTION)
	question_18 = models.CharField(max_length=1, choices=OPTION)
	question_19 = models.CharField(max_length=1, choices=OPTION)
	question_20 = models.CharField(max_length=1, choices=OPTION)
	
	question_21 = models.CharField(max_length=1, choices=OPTION)
	question_22 = models.CharField(max_length=1, choices=OPTION)
	question_23 = models.CharField(max_length=1, choices=OPTION)
	question_24 = models.CharField(max_length=1, choices=OPTION)
	question_25 = models.CharField(max_length=1, choices=OPTION)
	question_26 = models.CharField(max_length=1, choices=OPTION)
	question_27 = models.CharField(max_length=1, choices=OPTION)
	question_28 = models.CharField(max_length=1, choices=OPTION)
	question_29 = models.CharField(max_length=1, choices=OPTION)

	def __str__(self):
		return str(self.user_id) + " - " + str(self.question_1) + " - " + str(self.question_2) + " - " + str(self.question_2)
	
class UserProfile(models.Model):
	user_id = models.ForeignKey(User)
	timestamp = models.DateTimeField(default=datetime.now)

	OPTION = (
		('Rarely', 'Rarely(Several times a year)'), 
		('Occasionally', 'Occasionally(Several times a month)'),
		('Frequently', 'Frequently(Several times a week)'),
		('Very Frequently', 'Very Frequently(Several times a day)'),
		)

	OPTION_GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
		)

	age = models.IntegerField()
	gender = models.CharField(max_length=6, choices=OPTION_GENDER)
	occupation = models.CharField(max_length=100)
	field_of_study = models.CharField(max_length=50)
	simple_bar_chart = models.CharField(max_length=20, choices=OPTION)
	complex_bar_chart = models.CharField(max_length=20, choices=OPTION)

	def __str__(self):
		return str(self.user_id) + " - " + str(self.timestamp) + " - " + str(self.age) + " - " + str(self.gender) + " - " + str(self.occupation) + " - " + str(self.simple_bar_chart) + " - " + str(self.complex_bar_chart) + " - " + str(self.field_of_study)

	
	

