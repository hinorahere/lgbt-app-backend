# ![icons8-heart-rainbow-48](https://user-images.githubusercontent.com/25420200/144893690-d1c7764a-a2f2-4223-9bf4-adf80b9852ba.png) LGBT Dating App Backend ![icons8-heart-rainbow-48](https://user-images.githubusercontent.com/25420200/144893690-d1c7764a-a2f2-4223-9bf4-adf80b9852ba.png) 

### Requirements
- [Docker Engine](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Development set up

#### Clone Repo
```
git clone https://github.com/hinorahere/lgbt-app-backend.git
```
```
cd lgbt-app-backend
```

#### Create a virtual environment
```
python3 -m venv venv
```
```
source venv/bin/activate
```

#### Build the project
```
sudo docker-compose build
```
#### Run 
```
sudo docker-compose up
```

#### If successful, you should receive output similar to the following
![Screenshot from 2021-12-06 09-38-15](https://user-images.githubusercontent.com/25420200/144894805-7a5676e2-d0a9-40c3-bd5b-2426be33dca1.png)

#### Quit the server (ctrl+c)
#### Create a superuser
```
sudo docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
#### Serve again
```
sudo docker-compose up
```

#### Find the port number
![Screenshot from 2021-12-06 09-52-58](https://user-images.githubusercontent.com/25420200/144896820-2c2e83f6-c072-4a3c-babc-ce9669f4c7e4.png)

#### Using the assigned port number visit the following url and sign in with your superuser credentials
```
http://localhost:8000/admin/
```

## System Design
#### Reverse Proxy to Handle Static Media Files
![Blank diagram](https://user-images.githubusercontent.com/25420200/137376358-0e823b30-c633-421f-a780-605692f03ee9.png)

## API

### /api-token-auth/
* POST

##### Sample Body
```
{
    "username": "test@test.com",
    "password": "password"
}
```
#### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

### /api/user/
* GET
* POST

#### Sample Header
```
{
    "Authorization": "TOKEN <token>"
}
```

#### Sample Response
```
{
    "username": "<username>",
    "email": "<email>",
    "password": "<encrypted string>"
}
```

#### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

### /api/match_check/
* POST

#### Sample Body
```
{
    "prospective_id": 5
}
```

#### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
