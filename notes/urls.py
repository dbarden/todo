from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views

urlpatterns = patterns('',
                       url(r'^lists/$', views.ListView.as_view()),
                       url(r'^lists/(?P<pk>[0-9]+)/$', views.ListDetailView.as_view()),
                       url(r'^notes/$', views.NoteView.as_view()),
                       url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteDetailView.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
