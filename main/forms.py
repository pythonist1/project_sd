from django import forms

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.views import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm

from .models import AdvUser, user_registrated, Deal

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес эллектронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль еще раз для проверки')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    def clean_password(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        errors = {}
        contains = AdvUser.objects.filter(email=self.cleaned_data['email'])
        if contains:
            errors['email'] = ValidationError('e-mail уже зарегистрирован')
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors['password2'] = ValidationError(
                'Введенные  пароли не совпадают', code='password_mismatch')
        if errors:
            raise ValidationError(errors)


    def save(self, commit=True):
        user = super().save(commit=False)
        print(user.username, user.id)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')


class BBPasswordResetForm(PasswordResetForm):
    def clean(self):
        super().clean()
        contains = AdvUser.objects.filter(email=self.cleaned_data['email'])
        if not contains:
            raise ValidationError({'email': ValidationError('e-mail отсутствует в базе')})

class DateInput(forms.DateInput):
    input_type = 'date'

class BBCreateDeal(forms.ModelForm):
    name = forms.CharField(label='Наименование сделки')
    summ = forms.DecimalField(label='Стоимость сделки (руб.)', widget=forms.widgets.NumberInput)

    class Meta:
        model = Deal
        fields = ('__all__')
        widgets = {'author': forms.HiddenInput, 'author_role': forms.RadioSelect,
                   'type_of_deal': forms.RadioSelect, 'date': DateInput, 'commission_responce': forms.RadioSelect}

