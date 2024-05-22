from schemas.user import UserResponse
from test_main import client
import pytest


def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user_valid_input(mocker):
    mocker.patch("crud.user.create_user",
                 return_value={"id": 1, "name": "Test User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"})

    response = client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com", "comment": "Test comment",
              "organization": "Test Organization"},
    )

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"}


def test_get_user_by_id_valid_input(mocker):
    mocker.patch("crud.user.read_user",
                 return_value={"id": 1, "name": "Test User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"})

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"}


def test_update_user_valid_input(mocker):
    mocker.patch("crud.user.update_user",
                 return_value={"id": 1, "name": "Updated User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"})

    response = client.put(
        "/users/1",
        json={"name": "Updated User", "email": "test@example.com", "comment": "Test comment",
              "organization": "Test Organization"},
    )

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated User", "email": "test@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"}


def test_delete_user_valid_input(mocker):
    mocker.patch("crud.user.delete_user", return_value=None)

    response = client.delete("/users/1")
    assert response.status_code == 200
    response = client.get("/users/1")
    assert response.status_code == 404


def test_valid_user_email_and_user_create(mocker):
    mocker.patch("crud.user.read_user_by_email",
                 return_value=UserResponse(id=1, name="John", email="john@example.com", comment="Test comment",
                                           organization_id=1, organization_name="Test Organization"))

    response = client.post("/users/john@example.com",
                           json={"name": "John", "email": "john@example.com", "comment": "Test comment",
                                 "organization": "Test Organization"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John", "email": "john@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"}


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "John", "email": "john@example.com", "comment": "Test comment",
              "organization": "Test Organization"},
    )

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John", "email": "john@example.com", "comment": "Test comment",
                               "organization_id": 1, "organization_name": "Test Organization"}
