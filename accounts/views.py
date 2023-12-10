from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data= form.cleaned_data

            usuario = data.get('username')
            contrasenia= data.get('password')

            user = authenticate(username=usuario,password=contrasenia)

            if user:
                login(request, user)

        return redirect('RecetasList')
    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("RecetasList")

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
