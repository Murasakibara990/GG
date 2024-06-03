from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=250, unique=True)
    password = fields.CharField(max_length=250)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username


"""
Этот фрагмент кода определяет модель пользователя в Django.
В нем указаны четыре поля: id, username, password и created_at. Каждое поле соответствует определенному атрибуту пользователя.
  Например, username предназначен для хранения имени пользователя,
а password для хранения его пароля. Поле id используется как первичный ключ для идентификации каждого пользователя.
  Метод str переопределен для модели, чтобы возвращать имя пользователя в качестве его строкового представления.
  Это удобно для отображения объектов пользователей в административной панели Django и в других местах,
где объекты должны быть представлены в удобочитаемом формате.
"""


class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=250)
    created_at = fields.DatetimeField(auto_now_add=True)
    blogs = fields.ReverseRelation['Blog']

    def __str__(self):
        return self.name


"""Этот фрагмент кода определяет модель Category в Django. В модели определены три поля: id, name и created_at.
  Поле id используется как первичный ключ для идентификации каждой категории.
  Поле name предназначено для хранения названия категории, а поле created_at для хранения даты и времени создания категории.
  Также в модели определено обратное отношение (ReverseRelation) с моделью Blog. Это означает,
что у каждой категории может быть множество связанных с ней блогов.
  Метод str переопределен для модели, чтобы возвращать название категории в качестве ее строкового представления.
  Это удобно для отображения объектов категорий в административной панели Django и в других местах,
где объекты должны быть представлены в удобочитаемом формате."""


class Blog(models.Model):
    id = fields.IntField(pk=True)
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField('models.Category', related_name='blogs')
    title = fields.CharField(max_length=250)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.title
