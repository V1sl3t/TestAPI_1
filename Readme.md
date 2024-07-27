### Как получить объявления:

1. На url http://127.0.0.1:8000/api/users/ отправить Post-запрос с body:  
    {  
        "username": "username",  
        "password": "password"  
    }  

2. На url http://127.0.0.1:8000/api/jwt/create отправить Post-запрос с body:  
    {  
        "username": "username",  
        "password": "password"  
    }  

3. Можно получить данные объявления отправив Get-запрос на url http://127.0.0.1:8000/api/advertisement/{id}