from django.shortcuts import render
from django.http import HttpResponse
from .models import Villager
# Create your views here.

def home(request):

	sorting_type = 'name'

	if request.method == 'GET':
		if(request.GET.get('sort') == 'gender'):
			sorting_type = 'gender'
		if(request.GET.get('sort') == 'name'):
			sorting_type = 'name'
		if(request.GET.get('sort') == 'personality'):
			sorting_type = 'personality'
		if(request.GET.get('sort') == 'birthday'):
			sorting_type = 'birthday'
		if(request.GET.get('search')):
			search_string = request.GET.get('search')
			if search_string != ' ':
				villager_list = Villager.objects.filter(name__contains=search_string)
				context = {'villager_list' : villager_list}
				return render(request, 'villager_home/home.html', context)


	villager_list = Villager.objects.order_by(sorting_type)
	context = {'villager_list' : villager_list}
	return render(request, 'villager_home/home.html', context)