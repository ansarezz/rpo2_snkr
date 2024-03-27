from django.db import models

class Item(models.Model):
    name = models.CharField("Наименование товара", max_length=100)
    image = models.CharField('Ссылка', max_length=500)
    price = models.CharField("Цена", max_length=500)

    def __str__(self):
        return self.name