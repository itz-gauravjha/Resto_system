from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Cart, CartItem
from home_app.models import MenuItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_app:home")

        else:
            messages.success(request, ("There Was An Error Logging In, Try Again...."))
            return redirect("accounts:login")
    else:
        return render(request, "accounts/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out.."))
    return redirect("home_app:home")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request,user)
            messages.success(request, ("Registration Successful"))
            return redirect("home_app:home")
    else:
        form = RegisterUserForm()
    return render(request, "accounts/register_user.html", {'form':form})


@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart = cart, menu_item=menu_item)

    if not created:
        cart_item.quantity +=1 
        cart_item.save()
    return redirect('accounts:cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'accounts/cart_detail.html', {'cart':cart})

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    menu_item = get_object_or_404(MenuItem, id=item_id)
    cart_item = get_object_or_404(CartItem, cart=cart, menu_item=menu_item)

    if cart_item.quantity>1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('accounts:cart_detail')




