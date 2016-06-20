from django.shortcuts import render, redirect
from django.http import HttpResponse
from experiments.models import User, Locus, UserProfile
from experiments.forms import LocusForm, UserProfileForm


# Create your views here.
def index(request):
	all_users = User.objects.all()
	context = {'all_users': all_users}
	return render(request, 'experiments/index.html', context)

def new(request):
	new_user = User()
	new_user.save()
	request.session['user_id'] = new_user.id 
	return redirect('prestudy') 

def prestudy(request): 
	current_user_id = request.session['user_id']

	if request.method == 'POST':
		form = UserProfileForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_user_profile = UserProfile(
				user_id=User.objects.get(pk=current_user_id),
				age=cd['age'],
				occupation=cd['occupation'],
				field_of_study=cd['field_of_study'],
				simple_bar_chart=cd['simple_bar_chart'],
				complex_bar_chart=cd['complex_bar_chart'],
				)
			
			new_user_profile.save()
			return HttpResponse(new_user_profile) 
	else:
		form = UserProfileForm()

	context = {'user_id': current_user_id, 'form': form}
	return render(request, 'experiments/prestudy.html', context)


def existing_user(request):
	if 'existingid' in request.GET:
		if User.objects.filter(id= request.GET['existingid']):
			request.session['user_id'] = request.GET['existingid']
			return redirect('prestudy')
		else: 
			message = "Invalid user id"
	else: 
		message = "You submitted an empty form"
	return HttpResponse(message)


def locus(request): 
	current_user_id = request.session['user_id']

	if request.method == 'POST':
		form = LocusForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_locus = Locus(
				user_id=User.objects.get(pk=current_user_id),
				question_1=cd['question_1'],
				question_2=cd['question_1'],
				question_3=cd['question_1'],
				question_4=cd['question_1'],
				question_5=cd['question_1'],
				question_6=cd['question_1'],
				question_7=cd['question_1'],
				question_8=cd['question_1'],
				question_9=cd['question_1'],
				question_10=cd['question_1'],
				question_11=cd['question_1'],
				question_12=cd['question_1'],
				question_13=cd['question_1'],
				question_14=cd['question_1'],
				question_15=cd['question_1'],
				question_16=cd['question_1'],
				question_17=cd['question_1'],
				question_18=cd['question_1'],
				question_19=cd['question_1'],
				question_20=cd['question_1'],
				question_21=cd['question_1'],
				question_22=cd['question_1'],
				question_23=cd['question_1'],
				question_24=cd['question_1'],
				question_25=cd['question_1'],
				question_26=cd['question_1'],
				question_27=cd['question_1'],
				question_28=cd['question_1'],
				question_29=cd['question_1'],
				)

			new_locus.save()

			return HttpResponse(Locus.objects.all)
	else:
		form = LocusForm()

	context = {'user_id': current_user_id, 'form': form}
	return render(request, 'experiments/locus.html', context)





