from http import HTTPStatus
from typing import Annotated

from backend.database import get_session
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.models import User
from ..core.schemas import Message, UserList, UserPublic, UserSchema

router = APIRouter(prefix='/users', tags=['users'])
T_Session = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema, session: T_Session):
    query = select(User).where(
        (User.username == user.username) | (User.email == user.email)
    )
    db_user = await session.scalar(query)

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Email already exists',
        )

    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
    )

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.get('/', response_model=UserList)
async def read_users(session: T_Session, limit: int = 10, skip: int = 0):
    query = select(User).limit(limit).offset(skip)
    result = await session.scalars(query)
    return {'users': result.all()}


@router.put('/{user_id}', response_model=UserPublic)
async def update_user(
    user_id: int,
    user: UserSchema,
    session: T_Session,
):
    db_user = await session.scalar(select(User).where(User.id == user_id))
    
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db_user.email = user.email
    db_user.username = user.username
    db_user.password = user.password # Sem hash

    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.delete('/{user_id}', response_model=Message)
async def delete_user(
    user_id: int, 
    session: T_Session
):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    await session.delete(db_user)
    await session.commit()

    return {'message': 'User deleted'}