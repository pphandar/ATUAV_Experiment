from django.conf.urls import url 

from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new/', views.new, name='new'),
	url(r'^prestudy/', views.prestudy, name='prestudy'),
	url(r'^existing_user/', views.existing_user, name='existing_user'),
	url(r'^locus/', views.locus, name='locus'),
	url(r'^eyetracker/', views.eyetracker, name='eyetracker'),
]