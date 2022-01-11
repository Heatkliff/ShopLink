from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('settings/', user_views.SettingsView.as_view(), name='settings'),
    path('settings/password/', user_views.password, name='password'),
]
