from http import HTTPStatus
import pytest
from core.schemas import UserPublic

@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert data['username'] == 'testeusername'
    assert data['email'] == 'teste@teste.com'
    assert 'id' in data


@pytest.mark.asyncio
async def test_read_users(client, user):
    response = await client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    users = response.json()['users']
    assert any(u['id'] == user.id for u in users)


@pytest.mark.asyncio
async def test_update_user(client, user):
    response = await client.put(
        f'/users/{user.id}',
        json={
            'username': 'testeusername2',
            'email': 'test@test.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['username'] == 'testeusername2'
    assert data['email'] == 'test@test.com'
    assert data['id'] == user.id


@pytest.mark.asyncio
async def test_delete_user(client, user):
    response = await client.delete(f'/users/{user.id}')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


@pytest.mark.asyncio
async def test_delete_non_existent_user(client):
    response = await client.delete('/users/999')
    
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


@pytest.mark.asyncio
async def test_update_other_user(client, other_user):
    response = await client.put(
        f'/users/{other_user.id}',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()['username'] == 'bob'