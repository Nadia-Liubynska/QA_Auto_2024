import pytest


@pytest.mark.database
def test_database_connection(db_obj):
    db_obj.test_connection()


@pytest.mark.database
def test_check_all_users(db_obj):
    users = db_obj.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(db_obj):
    user = db_obj.get_user_address_by_name('Sergii')

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"
