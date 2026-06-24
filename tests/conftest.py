import copy
import pytest
from fastapi.testclient import TestClient

from app import app, activities as original_activities

_initial_activities = copy.deepcopy(original_activities)


@pytest.fixture
def client():
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities to their initial state before each test."""
    original_activities.clear()
    original_activities.update(copy.deepcopy(_initial_activities))
    yield
