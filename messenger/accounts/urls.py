from django.urls import path
from . import views


urlpatterns = [
	path('' , views.home_view , name = 'account'),
	path('registration' , views.reg_view , name = 'reg'),
	path('authorization', views.auth_view , name = 'auth'),
	path('settings' , views.settings_view , name = 'settings'),
	path('logout' , views.logout_view , name = 'logout'),
	path('change_password' , views.change_password_view , name = 'change_password'),
	path('search' , views.search_view , name = 'search'),
	path('message' , views.message_view , name = 'message')
]