from django.db import models

# Create your models here.
class Producto(models.Model):
	codigo = models.CharField(max_length=255)
	nombre = models.CharField(max_length=255)
	cantidad = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre