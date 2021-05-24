from django.conf.urls import url
from . import views

app_name = 'webapp'
urlpatterns = [
	url('first_page', views.first_page, name='first_page'),
	url('second_page', views.second_page, name='second_page'),
	url('', views.index, name='index')
]