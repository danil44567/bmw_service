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
    description = models.TextField(blank=False, verbose_name="Описание")
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, blank=False,)
    cover = models.ImageField(upload_to='сovers/', blank=False, verbose_name="Обложка")
    detail = models.TextField(blank=False, verbose_name="Детальное описание")
    dealer = models.CharField(max_length=255, blank=False, verbose_name="Ссылка на дилера")
    price = models.IntegerField(max_length=7, blank=False, verbose_name="Стоимость услуги")

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

class Request(models.Model):
    phone = models.CharField(max_length=20, blank=False, verbose_name="Телефон")
    name = models.CharField(max_length=20, blank=False, verbose_name="Имя")
    date = models.DateTimeField(blank=False, verbose_name="Дата заявки")
    services = models.ManyToManyField(Service,blank=True, verbose_name="Услуги")
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'

    def __str__(self):
        return f'{self.name} ({self.phone})'