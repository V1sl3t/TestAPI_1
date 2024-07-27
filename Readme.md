### Как получить объявления:

В терминале .../TestAPI_1/apitest:
1. python -m venv venv

2. source venv/Scripts/activate

3. pip install -r requirements.txt

4. python manage migrate

5. python manage.py loaddata db.json

6. python manage.py runserver

7. На url http://127.0.0.1:8000/api/users/ отправить Post-запрос с body:  
    {  
        "username": "username",  
        "password": "password"  
    }  

8. На url http://127.0.0.1:8000/api/jwt/create отправить Post-запрос с body:  
    {  
        "username": "username",  
        "password": "password"  
    }  

9. Можно получить данные объявления отправив Get-запрос на url http://127.0.0.1:8000/api/advertisement/{id}