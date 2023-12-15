from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm, FormularioCambioPassword
from accounts.models import Avatar

class DetalleUsuario(DetailView):
    model = User
    template_name = "accounts/detalle_usuario.html"


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia= data.get('password')

            user = authenticate(username=usuario,password=contrasenia)

            if user:
                login(request, user)

        return redirect('base')
    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("base")

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/register.html", contexto)

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()
            return redirect("RecetasList")

    form = UserUpdateForm(initial={"username": user.username, "email": user.email})
    contexto = {
        "form": form
    }
    return render(request, "accounts/register.html", contexto)



class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'accounts/passwordCambio.html'
    success_url = reverse_lazy('exitoso')


@login_required
def editar_avatar(request):
    user = request.user

    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.image = data["image"]
            except:
                avatar = Avatar(
                    user=user,
                    image=data["image"]
                )
            avatar.save()

            return redirect("RecetasList")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)
