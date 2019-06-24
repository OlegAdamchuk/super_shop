from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from tinymce import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='name', allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_abs_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


def image_up(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return f'{instance.slug}/{filename}'


class ProductManager(models.Manager):

    def all(self):
        return super(ProductManager, self).get_queryset().filter(availability=True)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = AutoSlugField(populate_from='title', allow_unicode=True, always_update=True, unique=True)
    short_desc = models.TextField(max_length=200, null=True, blank=True, verbose_name='Краткое описане')
    long_desc = HTMLField(verbose_name='Описание', default='')
    image = models.ImageField(upload_to=image_up, verbose_name='Изображение товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    availability = models.BooleanField(default=True, verbose_name='Доступен')
    objects = ProductManager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.title

    def get_abs_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})
