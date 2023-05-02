from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from uuid import UUID,uuid4
from models import Gender, Role, User, UpdateUser

app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Swetha",
        last_name="Theresa",
        gender=Gender.female,
        roles=[Role.admin, Role.user],
    ),
]

@app.get('/get_users')
async def get_users():
    return db

@app.post('/create_user')
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/delete/{id}')
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {'response': 'success'}
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")

@app.put("/update/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
        return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")