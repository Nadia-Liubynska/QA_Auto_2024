import pytest
from sqlite3 import IntegrityError, OperationalError


@pytest.mark.database
def test_database_connection(db):
    db.test_connection()


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(db):
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(db):
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(db):
    db.insert_product(4, 'печиво', 'солодке', 30)
    product_qnt = db.select_product_qnt_by_id(4)

    assert product_qnt[0][0] == 30

    db.delete_product_by_id(4)


@pytest.mark.database
def test_product_delete(db):
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(db):
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check if quantity of orders is equal to 1
    assert len(orders) == 1
    # Check data structure
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


# check that boolean values are converted into text or int
# depending on the column datatype
@pytest.mark.database
def test_insert_bool(db):
    db.insert_product(999, 'тестові', False, True)
    product = db.get_product(999)
    assert type(product[0][2]) is str
    assert type(product[0][3]) is int


# check that decimal values can't be inserted into the primary key column
@pytest.mark.database
def test_insert_decimal_into_primary_key(db):
    with pytest.raises(IntegrityError) as error:
        db.insert_product(9.9, 'тестові', 'дані', 10)
    assert "datatype mismatch" in str(error.value)
    assert "IntegrityError" in str(error.type)


# check that integer text values are converted to int
# if the column datatype is int
@pytest.mark.database
def test_insert_integer_text_into_quantity(db):
    db.insert_product(999, 'тестові', 'дані', '10')
    product = db.get_product(999)
    print(product)
    assert type(product[0][3]) is int


# check that text values can't be inserted
# if the column datatype is int
@pytest.mark.database
def test_insert_text_into_quantity(db):
    with pytest.raises(OperationalError) as error:
        db.insert_product(999, 'тестові', 'дані', 'abc')
    assert "no such column" in str(error.value)
    assert "OperationalError" in str(error.type)


# check that values in the id column are unique
@pytest.mark.database
def test_id_is_unique(db):
    db.insert_product(999, 'тестові', 'дані', 10)
    with pytest.raises(IntegrityError) as error:
        db.insert_product(999, 'тестові', 'дані', 10)
    assert "UNIQUE constraint failed" in str(error.value)
    assert "IntegrityError" in str(error.type)


# check that no error is raised if id does not exist
@pytest.mark.database
def test_non_existent_id(db):
    product = db.get_product(990)
    assert len(product) == 0


# check that valid id generates automatically
# if id is not specified upon row creation
@pytest.mark.database
def test_auto_add_id(db):
    db.auto_add_id('тестові_дані', 'без_ід', 10)
    product_list = db.get_all_products()
    assert product_list[-1][1] == 'тестові_дані'
    assert product_list[-1][2] == 'без_ід'
    db.delete_product_by_id(product_list[-1][0])


# TOOLBOX (comment these tests before running the entire set!)
# when you have a hammer everything looks like a nail
# (make custom requests for test creation purposes)
@pytest.mark.hammer
def test_hammer(db):
    query = "SELECT * FROM products"
    products = db.hammer(query)
    for line in products:
        print()
        for cell in line:
            print(f"{cell} type {type(cell)}")


# manually EVAPORATE your mistakes! and stray test data, I guess
@pytest.mark.evaporate
def test_EVAPORATE(db):
    query = "DELETE FROM products WHERE name = 'тестові'"
    db.hammer(query)
