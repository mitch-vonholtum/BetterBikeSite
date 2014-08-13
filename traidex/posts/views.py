from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from posts.models import Entry, Photo

def index(request):
	latest_entry_list = Entry.objects.all().order_by('-date')[:5]
	context = {'latest_entry_list' : latest_entry_list}
	return render(request, 'posts/index.html', context)

def detail(request, entry_id):
	entry = get_object_or_404(Entry, pk = entry_id)
	return render(request, 'posts/detail.html', {'entry' : entry})