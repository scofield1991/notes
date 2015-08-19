__author__ = 'oleksandr'
from django.conf.urls import patterns, url
from notesapp import views

urlpatterns=patterns('',
                     url(r'^$', views.index, name='index'),
                     url(r'^all_notes/$', views.all_notes, name='all_notes'),
                     url(r'^register/$', views.register, name='register'),
                     url(r'^login/$', views.auth_login, name='login'),
                     url(r'^logout/$', views.auth_logout, name='logout'),
                     url(r'^add_note/$', views.add_note, name='add_note'),
                     url(r'^note/(?P<note_id>[\w\-]+)/$', views.edit_note, name='edit_note'),
                     url(r'^del_note/(?P<note_id>[\w\-]+)/$', views.delete_note, name='delete_note'),
                     url(r'^see_note/(?P<note_id>[\w\-]+)/$', views.see_note, name='see_note'),
                     url(r'^add_label/$', views.add_label, name='add_label'),
)
