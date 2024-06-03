from pydantic import BaseModel
from datetime import datetime


class UserGet(BaseModel):
    id: int
    username: str
    created_at: datetime


class Login(BaseModel):
    username: str
    password: str


class Register(BaseModel):
    username: str
    password: str
    password2: str


class ChangePassword(BaseModel):
    password2: str
    password: str


class CategoryGet(BaseModel):
    id: int
    name: str
    created_at: datetime


class CategoryPost(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str = None


class BlogGet(BaseModel):
    id: int
    title: str
    content: float
    created_at: datetime


class BlogPost(BaseModel):
    title: str
    content: float
    category: int


class BlogUpdate(BaseModel):
    title: str = None
    content: float = None
    category: int = None


"""
Этот код использует библиотеку Pydantic для создания схем данных, которые определяют формат и типы данных,
ожидаемые при работе с различными запросами и ответами веб-приложения. Вот перечень классов с их описанием:

UserGet: Схема для получения данных о пользователе, включая идентификатор, имя пользователя и дату создания.
Login: Схема для входа пользователя, содержащая имя пользователя и пароль.
Register: Схема для регистрации нового пользователя, включающая имя пользователя, пароль и подтверждение пароля.
ChangePassword: Схема для изменения пароля пользователя, содержащая новый пароль и его подтверждение.
CategoryGet: Схема для получения данных о категории блога, включая идентификатор, название и дату создания.
CategoryPost: Схема для создания новой категории блога, содержащая только название.
CategoryUpdate: Схема для обновления информации о категории блога, позволяющая обновить только название.
BlogGet: Схема для получения данных о блоге, включая идентификатор, заголовок, содержание и дату создания.
BlogPost: Схема для создания нового блога, содержащая заголовок, содержание и идентификатор категории.
BlogUpdate: Схема для обновления информации о блоге, позволяющая обновить заголовок, содержание и/или категорию блога.
Такой подход позволяет структурировать данные, передаваемые между клиентом и сервером, обеспечивая их корректность и безопасность.
"""
