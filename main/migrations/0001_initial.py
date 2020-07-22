# Generated by Django 2.2.5 on 2019-11-12 10:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?')),
                ('available_score', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Доступно')),
                ('blocked_score', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Заблокировано')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Наименование сделки')),
                ('author', models.IntegerField()),
                ('partner', models.IntegerField(editable=False, null=True)),
                ('author_role', models.CharField(choices=[['Продавец', 'Продавец'], ['Покупатель', 'Покупатель']], default='Продавец', max_length=30, verbose_name='Ваша роль в сделке')),
                ('type_of_deal', models.CharField(choices=[['Товар', 'Товар'], ['Услуга', 'Услуга']], default='Товар', max_length=30, verbose_name='Тип сделки')),
                ('partner_email', models.EmailField(max_length=254, verbose_name='E-mail напарника')),
                ('description', models.TextField(null=True, verbose_name='Описание сделки')),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('date', models.DateTimeField(null=True, verbose_name='Срок сделки')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_done', models.BooleanField(default=False, editable=False)),
                ('score', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=15)),
                ('summ', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Стоимость сделки')),
                ('commission_responce', models.CharField(choices=[['Покупатель', 'Покупатель'], ['Продавец', 'Продавец'], ['50/50', '50/50']], default='Покупатель', max_length=30, verbose_name='Оплачивает комиссию')),
                ('partners', models.ManyToManyField(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
