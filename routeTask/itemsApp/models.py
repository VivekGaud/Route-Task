from django.db import models

# Create your models here.


class items(models.Model):

	item = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, blank=True, null=True)	
	class Meta:
		db_table = "rm55_items"