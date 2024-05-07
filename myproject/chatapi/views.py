from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth import authenticate, login
from .models import Chat
from django.contrib.auth.forms import UserCreationForm


# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if User.objects.filter(username=username).exists():
#             return HttpResponse("Username already exists")
#         myuser = User.objects.create(username=username, password=password) 
#         myuser.save()
#         return redirect('/login')
#     return render(request, 'registration_form.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username 
            user.save()
            login(request, user)
            return redirect('/chat')
            
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']  # Hashing should be added here for production
    #         if User.objects.filter(username=username).exists():
    #             return HttpResponse("Username already exists", status=400)
    #         # User.objects.create(username=username, password=password)
    #         user = User.objects.create(username=username)
    #         user.set_password(password=password)
    #         user.save()

    #         return HttpResponse('success')
    # else:
    #     form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})

def registration_success(request):
    return HttpResponse("Registration successful")


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponse('Successfully logged in!')
            # return redirect('/chat')
            print(User.tokens)
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login_form.html')


@csrf_exempt
def chat_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/login')

    # chats = Chat.objects.filter(user=user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Dummy response for AI chat."  # Simulate an AI response
        if user.tokens >= 100:
            user.tokens -= 100
            user.save()
            Chat.objects.create(user=user, message=message, response=response)
        else:
            return HttpResponse("Not enough tokens")
    return render(request, 'chat_form.html')

def token_balance(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'token_balance.html', {'tokens': request.user.tokens})
