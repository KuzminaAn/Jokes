import pytest


@pytest.fixture
def fixture_test_get_jokes_by_user_id_correct():
    user_id = 2
    return user_id


@pytest.fixture
def fixture_test_get_jokes_by_user_id_not_found():
    user_id = 500
    return user_id


@pytest.fixture
def fixture_test_get_jokes_by_joke_id_correct():
    joke_id = 1
    return joke_id


@pytest.fixture()
def fixture_test_get_jokes_by_joke_id_not_found():
    joke_id = 200
    return joke_id


@pytest.fixture()
def fixture_test_update_joke_correct():
    joke_id = 52
    return joke_id


@pytest.fixture()
def fixture_test_update_joke_not_found():
    joke_id = 300
    return joke_id


@pytest.fixture()
def fixture_test_delete_item_correct():
    joke_id = 19
    return joke_id


@pytest.fixture()
def fixture_test_delete_item_not_found():
    joke_id = 120
    return joke_id
