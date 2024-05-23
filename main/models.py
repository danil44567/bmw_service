from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя категории")

    class Meta:
        verbose_name = u'Категория услуги'
        verbose_name_plural = u'Категории услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя услуги")
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='сovers/', blank=True, verbose_name="Обложка")

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'

    def __str__(self):
        return self.name


class Promo(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Имя акции")
    description = models.TextField(blank=True, verbose_name="Описание")
    cover = models.ImageField(upload_to='сovers/promo/', blank=True, verbose_name="Обложка")

    class Meta:
        verbose_name = u'Акция'
        verbose_name_plural = u'Акции'

    def __str__(self):
        return self.name
