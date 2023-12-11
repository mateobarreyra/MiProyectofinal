from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request, register_request, editar_request, editar_avatar, DetalleUsuario, \
    CambioPassword

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('register/', register_request, name="Register"),
    path('edit/', editar_request, name="Edit"),
    path('avatar/', editar_avatar, name="Edit Avatar"),
    path('user/<int:pk>', DetalleUsuario.as_view(), name="UserDetail"),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordexito/', CambioPassword.as_view(template_name="accounts/passwordExitoso.html"), name='exitoso'),
]