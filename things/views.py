from django.shortcuts import render, redirect
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})


    # if request.method == 'POST':
    #     form = LogInForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('feed')
    #     messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    # form = LogInForm()
    # return render(request, 'log_in.html', {'form': form})