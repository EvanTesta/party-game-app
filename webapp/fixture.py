from game.models import *

User.objects.all().delete()
Challenges.objects.all().delete()

Challenges.objects.create(name="Draw a cat", rating="Easy")
Challenges.objects.create(name="Sing a song", rating="Medium")
Challenges.objects.create(name="Dance for 1 minute", rating="Easy")
Challenges.objects.create(name="Kiss a CONSENTING adult", rating="Hard")