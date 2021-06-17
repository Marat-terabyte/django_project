from django.db import models

class message_model(models.Model):
	message = models.CharField('Сообщения' , max_length = 250 , primary_key = True)

		