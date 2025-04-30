from django.db import models

class Mensagem(models.Model):
    texto = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]
