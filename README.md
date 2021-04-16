# Задание

Создать `django` учебное приложение. В нем не будет глубокого смысла, но мы сможет потренировать основные концепции.

Действия будут такими:

- По адресу `/user` можно отправить `GET` запрос с параметрами `firstname` и `lastname`, который вернет текстовый шаблон с фразой `Hello, $firstname $lastname!`. Запрос без параметров должен вернуть `Error!`
- По адресу `/time` django всегда отвечает на `GET` запрос: `Current time is $time`
- По адресу `/dump-settings` django возвращает весь список настроек, если `DEBUG=True`, иначе - ошибку доступа со статус кодом `403`

Технические требования:

- Необходимо использовать `django-split-setting` и `python-decouple`, секретные настройки хранятся отдельно 