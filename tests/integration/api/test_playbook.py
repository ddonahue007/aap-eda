import pytest
from rest_framework import status
from rest_framework.test import APIClient

from aap_eda.core import models

TEST_PLAYBOOK = """
---
- name: Test playbook
  hosts: all
  tasks: []
""".strip()


@pytest.mark.django_db
def test_list_playbooks(client: APIClient):
    obj = models.Playbook.objects.create(
        name="test-playbook.yml", playbook=TEST_PLAYBOOK
    )
    response = client.get("/eda/api/v1/playbooks")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {
            "id": obj.id,
            "project": None,
            "name": "test-playbook.yml",
            "playbook": TEST_PLAYBOOK,
        }
    ]


@pytest.mark.django_db
def test_create_playbook(client: APIClient):
    data_in = {
        "name": "test-playbook.yml",
        "playbook": TEST_PLAYBOOK,
    }
    response = client.post("/eda/api/v1/playbooks", data=data_in)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.data["id"]
    assert response.data == {
        "id": id_,
        "project": None,
        "name": "test-playbook.yml",
        "playbook": TEST_PLAYBOOK,
    }
    assert models.Playbook.objects.filter(pk=id_).exists()


@pytest.mark.xfail(reason="DRF ignores read only fields")
@pytest.mark.django_db
def test_create_playbook_with_id_fail(client: APIClient):
    data_in = {
        "id": 42,
        "name": "test-playbook.yml",
        "playbook": TEST_PLAYBOOK,
    }
    response = client.post("/eda/api/v1/playbooks", data=data_in)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_retrieve_playbook(client: APIClient):
    obj = models.Playbook.objects.create(
        name="test-playbook.yml", playbook=TEST_PLAYBOOK
    )
    response = client.get(f"/eda/api/v1/playbooks/{obj.id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": obj.id,
        "project": None,
        "name": "test-playbook.yml",
        "playbook": TEST_PLAYBOOK,
    }


@pytest.mark.django_db
def test_retrieve_playbook_not_exist(client: APIClient):
    response = client.get("/eda/api/v1/playbooks/42")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_destroy_playbook(client: APIClient):
    obj = models.Playbook.objects.create(
        name="test-playbook.yml", playbook=TEST_PLAYBOOK
    )
    response = client.delete(f"/eda/api/v1/playbooks/{obj.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not models.Playbook.objects.filter(pk=obj.id).exists()
