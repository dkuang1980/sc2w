from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignupForm


def signup(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = SignupForm()

    return render(
        request, 'registration/signup.html',
        context={
            'form': form,
            'next': redirect_to
        }
    )
