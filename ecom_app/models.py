from django.db import models


# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('smartphones', 'Смартфоны'),
        ('food', 'Еда'),
        ('furniture', 'Мебель'),
        ('other', 'Разное')
    )
    name = models.CharField(max_length=100, blank=True, null=False, verbose_name="Товар")
    description = models.TextField(max_length=3000, null=True, verbose_name='Описание')
    category = models.CharField(max_length=50, null=False, choices=CATEGORY_CHOICES, default='other',
                                verbose_name='Категория')
    quantity = models.IntegerField(default=0, blank=True, null=False, verbose_name='Остаток')
    image = models.CharField(max_length=3000, blank=True, null=False, verbose_name='Ссылка на фото')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']
