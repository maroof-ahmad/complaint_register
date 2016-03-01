from django.db import models

# Create your models here.

class Complain(models.Model):
	complain_text = models.TextField(max_length = 200)
	ELECTRICITY = 'EE'
	CARPENTARY = 'CP'
	SANITORY = 'ST'
	OTHERS = 'OT'

	COMPLAIN_TYPE = (
		(ELECTRICITY, 'Electricity'),
		(CARPENTARY, 'Carpentary'),
		(SANITORY, 'Sanitory'),
		(OTHERS, 'Others'),
		)

	complain_type = models.CharField(max_length = 2, 
		choices = COMPLAIN_TYPE, default = ELECTRICITY)
	id = models.AutoField(primary_key=True)
	room_no = models.CharField(max_length = 5)

	def __str__(self):
		return self.id
