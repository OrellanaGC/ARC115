from django.db import models

class Basurero(models.Model):
	codigo = models.TextField(verbose_name="Código")
	ubicacion = models.TextField(verbose_name="Ubicación")
	estado = models.TextField(verbose_name="Estado", default="Activo") 

	def __str__(self):
		return self.codigo
