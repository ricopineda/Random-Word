from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	# url(r'^word/$', views.index),
	url(r'^create$', views.create),
	# url('^(?P<word>\w+)$', views.show_word),

]