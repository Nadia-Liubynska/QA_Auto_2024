import pytest


# api basics tests
@pytest.mark.check
def test_change_name(user):
    assert user.name == "Nadia"


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == "Liubynska"
