import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal

from .utilities import send_activation_notification

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    available_score = models.DecimalField(verbose_name='Доступно', decimal_places=2, default=0.00, max_digits=10)

    blocked_score = models.DecimalField(verbose_name='Заблокировано', decimal_places=2, default=0.00, max_digits=10)


    class Meta(AbstractUser.Meta):
        pass

class Deal(models.Model):
    name = models.CharField(verbose_name='Наименование сделки', max_length=30, db_index=True)
    partners = models.ManyToManyField(AdvUser, editable=False)
    author = models.IntegerField()
    partner = models.IntegerField(editable=False, null=True)
    author_role = models.CharField(verbose_name='Ваша роль в сделке',
                                   choices=(['Продавец', 'Продавец'], ['Покупатель', 'Покупатель']),
                                   max_length=30, default='Продавец')
    type_of_deal = models.CharField(verbose_name='Тип сделки',
                                    choices=(['Товар','Товар'], ['Услуга', 'Услуга']),
                                    max_length=30, default='Товар')
    partner_email = models.EmailField(verbose_name='E-mail напарника')
    description = models.TextField(verbose_name='Описание сделки', null=True)
    date_debut = models.DateField(auto_now_add=True, editable=False)
    date = models.DateTimeField(verbose_name='Срок сделки', null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_done = models.BooleanField(default=False, editable=False)
    score = models.DecimalField(decimal_places=2, max_digits=15, default=0, editable=False)
    summ = models.DecimalField(verbose_name='Стоимость сделки', decimal_places=2, max_digits=15, default=0)
    commission_responce = models.CharField(verbose_name='Оплачивает комиссию', max_length=30,
                                           choices=(['Покупатель', 'Покупатель'], ['Продавец', 'Продавец'],
                                                    ['50/50','50/50']), default='Покупатель')



user_registrated = Signal(providing_args=['instance'])

def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registrated.connect(user_registrated_dispatcher)
# Create your models here.
