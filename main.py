from fastapi import FastAPI, Depends
from fastapi.responses import Response
from typing import List
from tortoise.contrib.fastapi import register_tortoise
from utils import create_access_token, get_current_user
from models import User, Category, Blog
from schemas import UserGet, CategoryGet, BlogGet, BlogPost, CategoryPost, BlogUpdate, CategoryUpdate, Register, \
    Login, ChangePassword

app = FastAPI()


@app.post("/register", status_code=201)
async def create_user(data: Register):
    if data.password != data.password2:
        return {"message": "Пароли не совпадают"}
    del data.password2
    user = await User.create(**data.dict())
    token = await create_access_token(user)
    data = UserGet(**user.__dict__).dict()
    data["access_token"] = token
    return data


# APP PATH= YO'LLI BILDIRADI
@app.post("/login")
async def login(data: Login):
    user = await User.get_or_none(username=data.username)
    if not user:
        return {'message': 'Неверное имя пользователя'}
    if data.password != user.password:
        return {'message': 'Неверный пароль'}
    token = await create_access_token(user)
    return {'access_token': token}


@app.patch("/change-password")
async def change_password(data: ChangePassword, user: User = Depends(get_current_user)):
    if data.password != data.password2:
        return {"message": "Пароли не совпадают"}
    user.password = data.password
    await user.save()
    return {'message': 'Пароль успешно обновлен'}


@app.get('/user', response_model=UserGet)
async def get_user(user: User = Depends(get_current_user)):
    return user


@app.delete("/user", status_code=204)
async def delete_user(user: User = Depends(get_current_user)):
    await user.delete()
    return {'message': 'Пользователь удалил'}


@app.post('/category', status_code=201)
async def create_category(data: CategoryPost):
    category = await Category.create(**data.dict())
    data = CategoryGet(**category.__dict__).dict()
    return data


@app.patch('/category/{pk}', response_model=CategoryGet)
async def category_update(pk: int, data: CategoryUpdate):
    data_dict = {k: v for k, v in data.dict().items() if v is not None}
    category = await Category.get_or_none(id=pk)
    if category:
        await category.update_from_dict(data_dict)
        await category.save()
        return category
    else:
        return Response({'success': False, 'message': 'Category not found'}, status_code=404)


@app.delete('/category/{pk}', status_code=204)
async def delete_category(pk: int):
    category = await Category.get_or_none(id=pk)
    if category:
        await category.delete()
        return {'success': True}
    else:
        return Response({'success': False, 'message': 'Category not found'}, status_code=404)

























# __________________________________________________________________________________________________________________________________________________________________


@app.post("/blog", status_code=201)
async def create_blog(data: BlogPost):
    data = data.dict()
    category = await Category.get_or_none(id=data['category'])
    data['category'] = category
    blog = await Blog.create(**data)
    data = BlogGet(**blog.__dict__).dict()
    return data


# __________________________________________________________________________________________________________________________________________________________________
























@app.get('/blog', response_model=List[BlogGet])
async def get_blog():
    blogs = await Blog.all()
    return blogs


@app.patch('/blog/{pk}', response_model=BlogGet)
async def income_update(pk: int, data: BlogUpdate):
    data_dict = {k: v for k, v in data.dict().items() if v is not None}
    blog = await Blog.get_or_none(id=pk)
    if blog:
        await blog.update_from_dict(data_dict)
        await blog.save()
        return blog
    else:
        return Response({'success': False, 'message': 'Blog not found'}, status_code=404)


@app.delete('/blog/{pk}', status_code=204)
async def delete_income(pk: int):
    blog = await Blog.get_or_none(id=pk)
    if blog:
        await blog.delete()
        return {'success': True}
    else:
        return Response({'success': False, 'message': 'Blog not found'}, status_code=404)


TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": ['aerich.models', 'models'],
            "default_connection": "default",
        },
    },
}
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True
)
"""
Этот код настраивает и использует Tortoise-ORM для работы с базой данных. Давайте разберем его по частям:

TORTOISE_ORM: Это словарь, определяющий конфигурацию Tortoise-ORM. В нем указываются параметры подключения к базе данных,
 такие как тип базы данных (в данном случае SQLite) и путь к файлу базы данных.
register_tortoise(): Это функция регистрации моделей и настройки Tortoise-ORM в приложении.
Она принимает несколько аргументов:
app: Экземпляр приложения (вероятно, Flask или FastAPI).
config: Конфигурация Tortoise-ORM, передаваемая как словарь TORTOISE_ORM.
generate_schemas=True: Флаг, указывающий на необходимость генерации схем базы данных на основе определенных моделей.
add_exception_handlers=True: Флаг, указывающий на добавление обработчиков исключений для Tortoise-ORM, чтобы обеспечить обработку ошибок.
Этот код используется для инициализации и настройки базы данных в приложении,
 что позволяет использовать модели данных и взаимодействовать с базой данных через Tortoise-ORM.
"""
