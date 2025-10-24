# party-game-app
This is a game intended to be played at parties. You need 1 laptop and everyone needs a phone. Run the server on the laptop and have people connect to it through their phone.
Players first select the level of challenge (easy, medium, or hard), and then they are given a challenge. Have a conversation with a stranger. If they complete then they are 
rewarded points. The player with the most points wins!
   
   The flow of the program is as follows: Login -> (select challenge -> challenge -> results) repeat
   
   Additional features include a Chat Room and Leaderboard.
## Dependencies
django  
daphne

## How to run
#### Get your ip address
Linux:
```
  ifconfig
```
Windows:
```
  ipconfig
```
Look for Wireless LAN adapter Wi-Fi:  
Then look for IPv4  

#### Migrations

```
python manage.py makemigrations game
```

```
python manage.py migrate
```

```
python manage.py shell < fixture.py 
```


#### To run the app
```
daphne -b 0.0.0.0 -p 8000 webapp.asgi:application
```
Then go to 
```
  http://<Your-Ip-Address>:8000
```

## Note
This is a lot of mr.GPT but I want to get this done so whatever
