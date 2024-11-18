from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField("Имя",max_length=50)
    email = models.EmailField("Почта", max_length=50, unique=True)
    phone = models.CharField("Телефон", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"





