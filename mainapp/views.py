from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def index(request):
    product = Product.objects.all()
    context = {"products":product}
    return render(request, 'mainapp/index.html', context)

def signin(request):
    return render(request, 'registration/login.html', context)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/")

# sign up user if they are not registered
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = { "form" : form }
    return render(request, 'registration/signup.html', context)

# def cart(request):
#     context = { 'title': 'Cart'}
#     return render(request, 'mainapp/cart.html', context)

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {"product":product}
    return render(request, 'mainapp/detail.html', context)

def search(request):
    query = request.GET['q']
    if query:
        product = Product.objects.filter(Q(title__icontains=query))
        context = {
            'title': 'Search Results',
            'products': product
        }
        return render(request, 'mainapp/search.html', context)
    else:
        product = Product.objects.all()
        context = {"products":product}
        return render(request, 'mainapp/index.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'mainapp/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
