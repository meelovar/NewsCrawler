Проверено на Ubuntu 23.04

# Запуск

Создать и активировать виртуальное окружение.

```shell
python -m venv venv
source venv/bin/activate
```

Установить необходимые пакеты.

```shell
python -m pip install -r requirements.txt
```

Выполнить main скрипт.

```shell
python main.py
```

Скрипт инициализирует БД, если это необходимо. Затем раз в 10 минут выполняет
обновление cookies.
