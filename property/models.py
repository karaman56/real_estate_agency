from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)

    owner_pure_phone = PhoneNumberField('Номер владельца', max_length=20, region='RU', blank=True, null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')
    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)
    has_balcony = models.BooleanField('Наличие балкона', db_index=True, null=True, blank=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка', null=True, blank=True,)
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_flats',
        verbose_name='Кто лайкнул',
        blank=True
    )


    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался',related_name='complaints')
    flat = models.ForeignKey(
        Flat, on_delete=models.CASCADE,
        verbose_name='Квартира, на которую жаловались',
        related_name='complaints'
    )
    text = models.TextField('Текст жалобы')
    created_at = models.DateTimeField('Дата создания', default=timezone.now)


    def __str__(self):
        return f"Жалоба от {self.user.email} на объявление #{self.flat.id}"


    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)

    pure_phone = PhoneNumberField('Номер владельца', max_length=20, region='RU', blank=True, null=True)
    flats = models.ManyToManyField(
        'Flat',
        related_name='owners',
        verbose_name='Квартиры в собственности',
        blank=True
    )


    def __str__(self):
        return self.name
