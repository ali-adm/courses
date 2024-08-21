from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Словарь для хранения курсов
courses = {
    1: {"name": "Python", "videos": 15},
    2: {"name": "Java", "videos": 10}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)  # Добавление аргумента для имени курса
parser.add_argument("videos", type=int)  # Добавление аргумента для количества видео

class Main(Resource):
    def get(self, course_id):
        # Если course_id равно 0, возвращаем все курсы
        if course_id == 0:
            return courses  # Возвращаем весь словарь курсов
        elif course_id in courses:
            return courses[course_id]  # Возвращаем курс по ID, если он существует
        else:
            return {"message": "Курс не найден"}, 404  # Ошибка 404, если курс не найден
    
    def delete(self, course_id):
        # Проверяем, существует ли курс перед удалением
        if course_id in courses:
            del courses[course_id]  # Удаляем курс по ID
            return {"message": "Курс удален"}, 200  # Возвращаем сообщение об успешном удалении
        else:
            return {"message": "Курс не найден"}, 404  # Ошибка 404, если курс не найден
    
    def post(self, course_id):
        # Проверяем, чтобы курс с таким ID не существовал
        if course_id in courses:
            return {"message": "Курс с таким ID уже существует"}, 400  # Ошибка 400, если курс уже существует
        courses[course_id] = parser.parse_args()  # Добавляем новый курс
        return courses[course_id], 201  # Возвращаем курс и статус 201 (создано)
    
    def put(self, course_id):
        # Будем обновлять курс только если он существует
        if course_id in courses:
            courses[course_id] = parser.parse_args()  # Обновляем курс
            return courses[course_id], 200  # Возвращаем обновленный курс и статус 200 (успешно)
        else:
            return {"message": "Курс не найден"}, 404  # Ошибка 404, если курс не найден

# Добавляем ресурс Main к API с маршрутом
api.add_resource(Main, "/api/courses/<int:course_id>")
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

"""
### Объяснение исправлений:

1. **Проверка существования курса**: 
   - В методах `get`, `delete`, `post`, и `put` добавлена проверка на существование курса перед выполнением операции.
   - В случае, если курс не найден, возвращается сообщение и код состояния HTTP (404).

2. **Обработка ошибок в POST**:
   - В методе `post` добавлена проверка на существование курса с одинаковым ID. Если такой курс уже существует, возвращается ошибка 400 (неправильный запрос).

3. **Возврат сообщений и статус-кодов**:
   - В каждом методе, помимо данных, теперь также возвращаются соответствующие сообщения и статус-коды, что делает API более информативным.

Эти изменения делают код более устойчивым и соответствующим стандартам проектирования RESTful API.
"""