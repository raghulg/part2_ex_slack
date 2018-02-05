from django.urls import path

from events import views

urlpatterns = [
	path('',views.index,name='index'),
	path('events',views.events_by_timePeriod, name='events_by_timePeriod'),
	path('name=<name>',views.events_by_engineer, name='events_by_engineer'),
	path('engineers',views.list_engineers, name='list_engineers'),
	path('summary/date=<event_date>',views.daily_summary, name='daily_summary'),
]
