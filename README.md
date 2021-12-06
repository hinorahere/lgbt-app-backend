# LGBT Dating App Backend

## Set up

### Clone Repo
```
git clone https://github.com/hinorahere/lgbt-app-backend.git
```

### Create a superuser
### cd into the root of the project directory and run
```
sudo docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### In the root of the project directory and run
```
sudo docker-compose build
```
```
sudo docker-compose up
```


## Reverse Proxy to Handle Static Media Files
![Blank diagram](https://user-images.githubusercontent.com/25420200/137376358-0e823b30-c633-421f-a780-605692f03ee9.png)
