from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from Users.models import Shop
from transliterate import translit

class Category(MPTTModel):
    """Модель описания древовидных категорий"""
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = "-".join(translit(str(self.name), language_code='ru', reversed=True).split())

        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    """Модель описания продукта"""
    category = TreeForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наменование')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default="123")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = "-".join(translit(str(self.name), language_code='ru', reversed=True).split()) + f"-{self.shop}"

        return super(Product, self).save(*args, **kwargs)