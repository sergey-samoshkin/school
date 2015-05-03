# school

Необходимые программы: virtualbox, vagrant, git

Исходники
```sh
git clone https://github.com/sergey-samoshkin/school.git
```

Создание виртуалки
```sh
vagrant up
```

Создание главного админа в админке
```sh
vagrant ssh -c "cd /vagrant/ && python3 manage.py createsuperuser"
```

Запуск веб-сервера
```sh
vagrant ssh -c "cd /vagrant/ && python3 manage.py runserver 0.0.0.0:8000"
```

Сайт:
http://localhost:8080/

Админка сайта:
http://localhost:8080/admin

Получение обновлений
```sh
git pull
```

Применение обновлений для базы данных
```sh
vagrant ssh -c "cd /vagrant/ && python3 manage.py migrate"
```

Очистка базы данных
```sh
vagrant ssh -c "cd /vagrant/ && python3 manage.py migrate schoolapp zero"
```

