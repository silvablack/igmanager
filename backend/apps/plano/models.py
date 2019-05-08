from django.db import models

# Create your models here.

class Plano(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title + ' | R$' + str(self.price)

class PlanoUsuario(models.Model):
    title = models.CharField(max_length=50)
    type_plan = models.ForeignKey(Plano, on_delete=models.CASCADE)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

