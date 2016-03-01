from django.db import models

# Create your models here.

class Complain(models.Model):
	complain_text = models.TextField(max_length = 200)

	COMPLAIN_TYPE = (
		('Electricity', 'Electricity'),
		('Carpentary', 'Carpentary'),
		('Sanitory', 'Sanitory'),
		('Others', 'Others'),
		)

	complain_type = models.CharField(max_length = 50, 
		choices = COMPLAIN_TYPE, default = 'Electricity')
	id = models.AutoField(primary_key=True)
	room_no = models.CharField(max_length = 5)
	timestamp = models.DateTimeField(auto_now_add= True, auto_now= False)

	def __unicode__(self):
		return self.room_no
