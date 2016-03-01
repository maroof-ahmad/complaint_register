from django import forms
from .models import Complain

class ComplainForm(forms.ModelForm):
	class Meta:
		model = Complain
		fields = ['complain_text', 'complain_type', 'room_no']