from django.shortcuts import render
from django.http import JsonResponse
from game.models import User, Challenges
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def chat_room(request):
    user = User.objects.filter(real_name=request.session.get("real_name")).first()
    username = user.username if user else "Anonymous"
    return render(request, 'chat_room.html', {"username": username})

def login(request):
    if request.session.get("real_name"):
        print(request.session.get("real_name"))
        return render(request, 'game.html')
    else:
        return render(request, 'login.html')

def game(request):
    return render(request, 'game.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def process_result(request):
    if request.method == "POST":
        result = request.POST.get("result")
        rating = request.POST.get("rating")
        user = User.objects.filter(real_name = request.session.get("real_name")).first()
        success = False
        
        if result == "Completed":
            if rating == "Easy":
                user.score += 1
            elif rating == "Medium":
                user.score += 2
            elif rating == "Hard":
                user.score += 3
            success = True
        elif result == "Failed":
            user.score -= 1

        user.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "leaderboard",  # same name as in your consumer
            {"type": "leaderboard.update"}
        )

        context = {
            "success": success,
            "current_score": user.score
        }
        return render(request, "process_result.html", context)

def get_challenge(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")  # "Easy", "Medium", or "Hard"
        challenge = Challenges.objects.filter(rating=difficulty).order_by('?').first()
        return render(request, "challenge.html", {"challenge": challenge, "rating": difficulty})
    return render(request, "game.html")

def submit_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        real_name = request.POST.get("real_name")

        if User.objects.filter(real_name=real_name).exists():
            return JsonResponse({
                "success": False,
                "message": f"{real_name} is already in the game"
            })
        else:
            user = User.objects.create(username=username, real_name=real_name)
            User.save(user)

            # Store in session for 1 day
            request.session["real_name"] = real_name
            request.session.set_expiry(36000)

            return JsonResponse({
                "success": True,
                "message": f"{username} added to the game"
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid request"
    })
