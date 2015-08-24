__author__ = 'oleksandr'
from django.conf.urls import url
from notesapi import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.UserViewSet.as_view()),
    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^register/$', views.UserRegistration.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]