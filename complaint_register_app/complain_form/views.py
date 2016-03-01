from django.shortcuts import render
from .forms import ComplainForm
from .models import Complain

# Create your views here.
def complain(request):
	form = ComplainForm(request.POST or None)



	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		form = ComplainForm()

	context = {
		"form" : form
	}

	return render(request, "complainform.html", context)

def home(request):
	complains = Complain.objects.all()
	context = {
		"complains" : complains
	}
	return render(request, "home.html", context)
