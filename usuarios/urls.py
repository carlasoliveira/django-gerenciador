from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
	path('login/', LoginView.as_view(template_name = 'cadastros/form.html',
								  extra_context={'title' : 'Entrar',
						 						'name_button' : 'Login'}), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('alterar-senha/', PasswordChangeView.as_view(template_name = 'cadastros/form.html', 
												   extra_context = {'title': 'Alterar senha', 
																	'name_button': 'Alterar'}), name='alterar-senha'),
]