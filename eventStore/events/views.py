from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

from datetime import datetime
import json

from events.models import Deploys

def index(request):
	return render(request, 'index.html', context = {})

def events_by_engineer(request, name):
	try:
		result = list(Deploys.objects.filter(engineer = name).values('id','sha','date','action'))
	except ObjectDoesNotExist:
		raise Http404("Data object not found")
	else:
		return HttpResponse (json.dumps(result), content_type='application/json')

def list_engineers(request):
	try:
		result = list(Deploys.objects.all().values('engineer').distinct())
	except ObjectDoesNotExist:
        	raise Http404("Data object not found")
	else:
		return HttpResponse (json.dumps(result), content_type='application/json')

def daily_summary(request, event_date):	
	#checking if the date input is valid
	if (len(event_date) != 8):
		raise Http404("Incorrect DATE input")

	try:
		a_time = datetime.strptime(event_date,'%Y%m%d')
		start_time_sec = int(a_time.strftime('%s'))
		end_time_sec = start_time_sec + 86400
	except ValueError:
		raise Http404("Incorrect DATE input")

	try:
		result = list(Deploys.objects.filter(date__gte = start_time_sec,date__lte = end_time_sec).values('action').annotate(number_of_events=Count('action')))
	except ObjectDoesNotExist:
        	raise Http404("Data object not found")
	else:
		return HttpResponse (json.dumps(result), content_type='application/json')


def events_by_timePeriod(request):

	try:	
		start_date = request.GET['start_date']
		start_time = request.GET['start_time']
		end_date = request.GET['end_date']	
		end_time = request.GET['end_time']	
	except:
		raise Http404("Missing required field")	

	if (len(start_date) != 8 or len(end_date)!=8 ):
                raise Http404("Incorrect DATE input")
	
	start = start_date + ' ' + start_time;
	end = end_date + ' ' + end_time;
	
	
	try:
               	s_time = datetime.strptime(start,'%Y%m%d %H:%M:%S')
                start_datetime = int(s_time.strftime('%s'))
                e_time = datetime.strptime(end,'%Y%m%d %H:%M:%S')
               	end_datetime = int(e_time.strftime('%s'))
	except ValueError:
		raise Http404("Incorrect DATE input")

	try:
		result = list(Deploys.objects.filter(date__gte = start_datetime,date__lte = end_datetime).values('id','sha','date','action','engineer'))
	except ObjectDoesNotExist:
		raise Http404("Data object not found")
	else:
		return HttpResponse (json.dumps(result), content_type='application/json')


