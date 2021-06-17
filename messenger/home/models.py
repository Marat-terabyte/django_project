from django.db import models

class citata_model(models.Model):
	citata = models.CharField(max_length = 600 )
	author = models.CharField(max_length = 100 )
	