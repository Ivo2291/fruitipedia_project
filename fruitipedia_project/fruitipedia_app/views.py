from django.shortcuts import render, redirect

from fruitipedia_project.fruitipedia_app.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, \
    FruitDeleteForm, ProfileEditForm
from fruitipedia_project.fruitipedia_app.models import ProfileModel, FruitModel


def get_profile():
    try:
        return ProfileModel.objects.get()

    except ProfileModel.DoesNotExist as ex:

        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    context = {
        'fruits': fruits,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)


def fruit_create(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit,
    }
    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'delete-fruit.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    fruits_count = FruitModel.objects.count()

    context = {
        'profile': profile,
        'fruits_count': fruits_count
    }

    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()

        return redirect('index')

    return render(request, 'delete-profile.html')
