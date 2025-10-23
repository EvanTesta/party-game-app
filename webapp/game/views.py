from django.shortcuts import render

def chat_room(request):
    return render(request, 'chat_room.html')

def login(request):
    return render(request, 'login.html')

def game(request):
    return render(request, 'game.html')
