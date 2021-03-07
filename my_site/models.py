from django.db import models

# Create your models here.
class Produtos(models.Model):
    data = models.DateField(auto_now_add=True)
    produto = models.CharField(max_length=40)
    quantidade = models.DecimalField(max_digits=5, decimal_places=0)
    preço = models.DecimalField(max_digits=7, decimal_places=2)
    descrição = models.TextField(blank=False, null=False)

    class Meta:

        verbose_name_plural = "Produtos"

    def __str__(self):

        return self.produto

class Sobre_Nos(models.Model):
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=20)
    texto = models.TextField(blank=False, null=False)

    class Meta:

        verbose_name_plural = "Sobre Nós"

    def __str__(self):

        return self.titulo