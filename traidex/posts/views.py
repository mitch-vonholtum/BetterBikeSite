from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from django.core.urlresolvers import reverse

from posts.models import Entry, Photo

def index(request):
	latest_entry_list = Entry.objects.all().order_by('-date')[:5]
	context = {'latest_entry_list' : latest_entry_list}
	return render(request, 'posts/index.html', context)

def detail(request, entry_id):
	entry = get_object_or_404(Entry, pk = entry_id)
	return render(request, 'posts/detail.html', {'entry' : entry})

def create(request):

	if request.method == 'GET':
		return render(request, 'posts/create.html')

	elif request.method == 'POST':
		#Gather POST data from form
		trail_name = request.POST['trail_name']
		post_text = request.POST['text_post']
		
		#Need to validate this and put it behind some kind of flow control
		entry = Entry()
		entry.state = 'SD'
		entry.city = 'Sioux Falls'
		entry.text_post = post_text #This seems unreasonably confusing
		entry.user = 'Armadillus'
		entry.date = timezone.now()
		entry.title = trail_name
		entry.trail_type = 'Paved'
		entry.save()
		return HttpResponseRedirect(reverse('posts:index'))