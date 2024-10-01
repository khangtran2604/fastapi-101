import os

os.environ["IS_TESTING"] = "True"
os.environ["DB_NAME"] = ":memory:"

import pytest

from data.user import create_user
from dto.user import CreateUser
from model.user import User


@pytest.fixture
def created_user() -> User:
    return User(id="123", fullname="Test User", username="test", password="test")

def create_user_success(created_user: User):
    user_data = CreateUser(username=created_user.username, password=created_user.password, fullname=created_user.fullname)
    new_user = create_user(user_data)

    assert new_user.username == created_user.username
    assert new_user.fullname == created_user.fullname
