from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

class Entry(models.Model):

	#Fixing the plural so it doesn't show up as 'entrys' because that is bothersome
	class Meta:
		verbose_name_plural = 'entries'

	state = USStateField(null = True, blank = True, max_length = 2)
	city = models.CharField(max_length=100)
	text_post = models.CharField(max_length = 2000)
	user = models.CharField(max_length = 50)
	date = models.DateTimeField('publication date')
	title = models.CharField(max_length = 50)

	#constants for trail type choices
	#This seems... roundabout, but whatever.
	GRAVEL = 'Gravel'
	PAVED = 'Paved'
	DIRT = 'Dirt'
	TRAIL_TYPE_CHOICES = (
		(GRAVEL, 'Gravel'),
		(PAVED, 'Paved'),
		(DIRT, 'Dirt'),
	)

	trail_type = models.CharField(max_length = 6, choices = TRAIL_TYPE_CHOICES)

	#More descriptive representation of this object
	def __unicode__(self):
		return 'Trail entry: ' + self.title

class Photo(models.Model):
	photo = models.ImageField(upload_to='photos') #OOER MAN I DUNNO HOW THIS WORKS
	entry = models.ForeignKey(Entry) #This corresponds to one entry.

	#More descriptive representation of this object
	def __unicode__(self):
		return 'Photo for trail entry'