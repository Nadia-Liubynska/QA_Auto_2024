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


@pytest.mark.database
@pytest.mark.wip
def test_product_qnt_update(db_obj):
    db_obj.update_product_qnt_by_id(1, 25)
    water_qnt = db_obj.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25
