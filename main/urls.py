from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView

from .views import index, other_page, BBLoginView, profile, BBLogoutView, \
    ChangeUserInfoView, BBPasswordChangeView, \
    RegisterDoneView, RegisterUserView, \
    user_activate, DeleteUserView, BBPasswordResetView, \
    BBPasswordResetConfirmView, personal, createdeal

app_name = 'main'
urlpatterns = [
    path('accounts/create_deal/', createdeal, name='create_deal'),
    path('accounts/personal/', personal, name='personal'),
    path('accounts/password/reset/', BBPasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/',
         BBPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(),
         name='register'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(),
         name='profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/delete/', DeleteUserView.as_view(),
         name='profile_delete'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]