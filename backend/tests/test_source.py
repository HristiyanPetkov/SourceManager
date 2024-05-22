from models.source import Source
from schemas.source import SourceType
from test_main import client


def test_get_all_source():
    response = client.get("/sources/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_valid_source(mocker):
    mocker.patch("crud.source.create_source",
                 return_value=Source(id=1, type=SourceType.ip, value="192.168.10.1", comment="Test source",
                                     organization_id=1, user_id=1))

    response = client.post(
        "/sources/",
        json={
            "type": "ip",
            "value": "192.168.10.1",
            "comment": "Test source",
            "organization_id": 1,
            "user_id": 1
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "type": "ip",
        "value": "192.168.10.1",
        "comment": "Test source",
        "organization_id": 1,
        "user_id": 1
    }


def test_create_invalid_source():
    response = client.post(
        "/sources/",
        json={
            "type": "email",
            "value": "test@example.com",
            "comment": "Test source",
            "organization_id": 1,
            "user_id": 1
        }
    )

    print(response.json())

    assert response.status_code == 422


def test_update_source_valid_input(mocker):
    mocker.patch("crud.source.update_source",
                 return_value=Source(id=1, type=SourceType.ip, value="192.168.10.1", comment="Test source",
                                     organization_id=1, user_id=1))

    response = client.put(
        "/sources/1",
        json={
            "type": "ip",
            "value": "192.168.10.1",
            "comment": "Test source",
            "organization_id": 1,
            "user_id": 1
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "type": "ip",
        "value": "192.168.10.1",
        "comment": "Test source",
        "organization_id": 1,
        "user_id": 1
    }


def test_delete_source_valid_input(mocker):
    mocker.patch("crud.source.delete_source", return_value=None)

    response = client.delete("/sources/1")
    assert response.status_code == 200
    response = client.get("/sources/1")
    assert response.status_code == 404


def test_get_source_by_id_valid_input(mocker):
    mocker.patch("crud.source.read_source",
                 return_value=Source(id=1, type=SourceType.ip, value="192.168.10.1", comment="Test source",
                                     organization_id=1, user_id=1))

    response = client.get("/sources/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "type": "ip",
        "value": "192.168.10.1",
        "comment": "Test source",
        "organization_id": 1,
        "user_id": 1
    }


def test_valid_source_type_and_organization_id(mocker, source_crud=None):
    mocker.patch("crud.source.read_source_by_type",
                 return_value=[Source(id=1, type=SourceType.ip, value="192.168.10.1", comment="Test source",
                                      organization_id=1, user_id=1)])

    response = client.get("/sources/ip/1")

    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "type": "ip",
        "value": "192.168.10.1",
        "comment": "Test source",
        "organization_id": 1,
        "user_id": 1
    }]


def test_create_source():
    response = client.post(
        "/sources/",
        json={
            "type": "ip",
            "value": "192.168.10.1",
            "comment": "Test source",
            "organization_id": 1,
            "user_id": 1
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "type": "ip",
        "value": "192.168.10.1",
        "comment": "Test source",
        "organization_id": 1,
        "user_id": 1
    }