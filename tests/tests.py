from fastapi.testclient import TestClient

from src.app.main import app
from src.db.functions import get_jokes_by_id, get_jokes_by_user
from tests.test_vars import Variable

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, my friend!"}


def test_get_jokes_by_user_id_correct(fixture_test_get_jokes_by_user_id_correct):
    user_id = fixture_test_get_jokes_by_user_id_correct
    response = client.get("/joke/", headers={"X-User": str(user_id)})
    assert response.status_code == 200
    assert len(response.json()) == len(get_jokes_by_user(user_id))

    data1 = response.json()
    data2 = get_jokes_by_user(user_id)
    for i in data2:
        assert i.dict() in data1


def test_get_jokes_by_user_id_not_found(fixture_test_get_jokes_by_user_id_not_found):
    user_id = fixture_test_get_jokes_by_user_id_not_found
    response = client.get("/joke/", headers={"X-User": str(user_id)})
    assert response.status_code == 404


def test_get_jokes_by_joke_id_correct(fixture_test_get_jokes_by_joke_id_correct):
    joke_id = fixture_test_get_jokes_by_joke_id_correct
    response = client.get(f"/joke/{joke_id}")
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()


def test_get_jokes_by_joke_id_not_found(fixture_test_get_jokes_by_joke_id_not_found):
    joke_id = fixture_test_get_jokes_by_joke_id_not_found
    response = client.get(f"/joke/{joke_id}")
    assert response.status_code == 404


def test_create_joke():
    response = client.post(
        "/joke/",
        headers=Variable.header_create,
        json=Variable.json_create,
    )
    data = response.json()
    joke_id = data["joke_id"]
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()


def test_update_joke_correct(fixture_test_update_joke_correct):
    joke_id = fixture_test_update_joke_correct
    response = client.put(
        f"/joke/{joke_id}",
        json=Variable.json_update,
    )
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()


def test_update_joke_not_found(fixture_test_update_joke_not_found):
    joke_id = fixture_test_update_joke_not_found
    response = client.put(
        f"/joke/{joke_id}",
        json=Variable.json_update,
    )
    assert response.status_code == 404


def test_delete_item_correct(fixture_test_delete_item_correct):
    joke_id = fixture_test_delete_item_correct
    response = client.delete(f"/joke/{joke_id}")
    assert response.status_code == 204


def test_delete_item_not_found(fixture_test_delete_item_not_found):
    joke_id = fixture_test_delete_item_not_found
    response = client.delete(f"/joke/{joke_id}")
    assert response.status_code == 404


def test_create_random_joke():
    response = client.post(
        "/joke/random",
        headers=Variable.header_random,
    )
    data = response.json()
    joke_id = data["joke_id"]
    assert response.status_code == 200
    assert response.json() == get_jokes_by_id(joke_id).dict()
