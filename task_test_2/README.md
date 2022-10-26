Приложение на базе Django 3.1.14
Технические требования 

 Django 3.1+, DRF 3+
 PostgreSQL 12+
 Python 3.8+
 aiohttp 3.7+
 PyDantic 1.9+

Запуск проекта осуществляется в Docker.

docker-compose build
docker-compose

Адрес для одного артикула:
/api/v1/article/
Адрес для обработки файла articles.xlsx
/api/v1/loading/excel/