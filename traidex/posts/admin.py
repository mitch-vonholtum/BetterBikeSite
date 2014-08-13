from django.contrib import admin
from posts.models import Entry, Photo
from django import forms

#The following two classes set the widget for
#the text post in the admin page to a text area,
#for increased readability and stuff.
class TextPostForm(forms.ModelForm):
	text_post = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Entry

class TextPostAdmin(admin.ModelAdmin):
	form = TextPostForm

#Registering models for use on admin page
admin.site.register(Entry, TextPostAdmin)
admin.site.register(Photo)

