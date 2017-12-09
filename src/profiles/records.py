from django.db import models
from django.conf import settings

class Record(models.Model):
    tweet = models.CharField(max_length=255, unique=True)
    score = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
      return self.tweet

    def save(self, *args, **kwargs):
    	self.full_clean()
    	super(Record, self).save(*args,**kwargs)

    def delete(self, *args, **kwargs):
    	self.full_clean()
    	super(Record, self).delete(*args,**kwargs)



