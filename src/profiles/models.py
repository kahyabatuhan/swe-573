from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='My description', null=True, blank=True)
	#location = models.CharField(max_length=120)
	#job = models.CharField(max_length=120, default = 'Some Default')
	#job2 = models.CharField(max_length=120, null=True, blank=False)
	def __unicode__(self):
		return self.name
		