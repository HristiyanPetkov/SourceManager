from test_main import client


def test_get_all_organizations():
    response = client.get("/organizations/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_organization():
    response = client.post(
        "/organizations/",
        json={"name": "Test Organization"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Organization"}


def test_get_organization():
    response = client.get("/organizations/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Organization"}


def test_update_organization():
    response = client.put(
        "/organizations/1",
        json={"name": "Updated Organization"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Organization"}


def test_delete_organization():
    response = client.delete("/organizations/1")
    assert response.status_code == 200
    response = client.get("/organizations/1")
    assert response.status_code == 404


def test_get_organization_by_id():
    response = client.get("/organizations/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Organization not found"}
