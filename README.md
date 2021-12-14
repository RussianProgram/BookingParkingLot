# BookingParkingLotTestWork

## Как запустить
### Первоначальная установка 
```
cd BookingParkingLotTestWork
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
Создаём супер-юзера с именем admin и паролем admin.


## Описание API

См. [API.md](API.md)

# Ссылка на рабочий проект: http://russianprogram.pythonanywhere.com/
```
/parking-lot/list
/parking-lot/detail/<slot_number>
...

```
