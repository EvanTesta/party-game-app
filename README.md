# party-game-app

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
