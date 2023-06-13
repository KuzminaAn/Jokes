from fastapi.testclient import TestClient
from main import app
from functions import get_jokes_by_user, get_jokes_by_id


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, my friend!"}


def test_get_jokes_by_user_id():
    user_id = 5
    response = client.get(
        "/joke/",
        headers={'X-User': str(user_id)}
    )
    assert response.status_code == 200
    assert len(response.json()) == len(get_jokes_by_user(user_id))

    data1 = response.json()
    data2 = get_jokes_by_user(user_id)
    for i in data2:
        assert i.dict() in data1


def test_get_jokes_by_joke_id():
    joke_id = 2
    response = client.get(f"/joke/{joke_id}")
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()


def test_create_joke():
    response = client.post(
        "/joke/",
        headers={'X-User': '1'},
        json={'joke_content': 'smth1', 'joke_author': 'smth2'}
    )
    data = response.json()
    joke_id = data['joke_id']
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()


def test_update_joke():
    joke_id = 11
    response = client.put(
        f"/joke/{joke_id}",
        json={'joke_content': 'smth3', 'joke_author': 'smth4'}
    )
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()



def test_delete_item():
    response = client.delete("/joke/1")
    assert response.status_code == 204


def test_create_random_joke():
    response = client.post(
        "/joke/random",
        headers={'X-User': '1'},
    )
    data = response.json()
    joke_id = data['joke_id']
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()
