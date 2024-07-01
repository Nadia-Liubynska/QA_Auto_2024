import pytest
from sqlite3 import IntegrityError, OperationalError


# api database tests
@pytest.mark.database
def test_database_connection(db):
    db.test_connection()


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_by_name(db):
    name = 'Sergii'

    user = db.get_user_address_by_name(name)

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(db):
    product_id = 1
    qnt = 25

    db.update_product_qnt_by_id(product_id, qnt)

    water_qnt = db.select_product_qnt_by_id(product_id)

    assert water_qnt[0][0] == qnt


@pytest.mark.database
def test_product_insert(db):
    product_id = 4
    name = 'печиво'
    desc = 'солодке'
    qnt = 30

    db.insert_product(product_id, name, desc, qnt)

    product_qnt = db.select_product_qnt_by_id(product_id)

    assert product_qnt[0][0] == qnt

    # id in this test does not match usual test id (999)
    # defined in the Database class, and needs to be specified
    # for the successful teardown
    db.test_id = product_id


@pytest.mark.database
def test_product_delete(db):
    product_id = 99
    name = 'тестові'
    desc = 'дані'
    qnt = 999

    db.insert_product(product_id, name, desc, qnt)

    db.delete_product_by_id(product_id)

    qnt = db.select_product_qnt_by_id(qnt)

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


# INDIVIDUAL ASSIGMENT

# refer to the db_test_cases.xlsx in the root directory for the ids,
# summaries, steps, test data, and expected results

# ID 1
# check that boolean values are converted into str or int
# depending on the column datatype
@pytest.mark.database
def test_insert_bool(db):
    product_id = 999
    name = 'тестові'
    desc = False
    qnt = True

    db.insert_product(product_id, name, desc, qnt)

    product = db.get_product(product_id)

    assert type(product[0][2]) is str
    assert type(product[0][3]) is int


# ID 2
# check that decimal values can't be inserted into the primary key column
@pytest.mark.database
def test_insert_decimal_into_primary_key(db):
    product_id = 9.9
    name = 'тестові'
    desc = 'дані'
    qnt = 10

    with pytest.raises(IntegrityError) as error:
        db.insert_product(product_id, name, desc, qnt)

    assert "datatype mismatch" in str(error.value)
    assert "IntegrityError" in str(error.type)


# ID 3
# check that integer text values are converted to int
# if the column datatype is int
@pytest.mark.database
def test_insert_integer_text_into_quantity(db):
    product_id = 999
    name = 'тестові'
    desc = 'дані'
    qnt = '10'

    db.insert_product(product_id, name, desc, qnt)

    product = db.get_product(product_id)

    assert type(product[0][3]) is int


# ID 4
# check that text values can't be inserted
# if the column datatype is int
@pytest.mark.database
def test_insert_text_into_quantity(db):
    product_id = 999
    name = 'тестові'
    desc = 'дані'
    qnt = 'abc'

    with pytest.raises(OperationalError) as error:
        db.insert_product(product_id, name, desc, qnt)

    assert "no such column" in str(error.value)
    assert "OperationalError" in str(error.type)


# ID 5
# check that values in the id column are unique
@pytest.mark.database
def test_id_is_unique(db):
    product_id = 999
    name = 'тестові'
    desc = 'дані'
    qnt = 10

    db.insert_product(product_id, name, desc, qnt)

    with pytest.raises(IntegrityError) as error:
        db.insert_product(product_id, name, desc, qnt)

    assert "UNIQUE constraint failed" in str(error.value)
    assert "IntegrityError" in str(error.type)


# ID 6
# check that no error is raised if id does not exist
@pytest.mark.database
def test_non_existent_id(db):
    non_existing_product_id = 990

    product = db.get_product(non_existing_product_id)

    assert len(product) == 0


# ID 7
# check that valid id generates automatically
# if id is not specified in the row creation query
@pytest.mark.database
def test_auto_add_id(db):
    # get list of all the products in the table, find id of the last product
    product_list = db.get_all_products()
    last_id = product_list[-1][0]

    # add a product without specifying the id
    name = 'тестові_дані'
    desc = 'без_ід'
    qnt = 10

    db.auto_add_id(name, desc, qnt)

    # get list of all the products again
    product_list = db.get_all_products()

    # check that the last product on the table is a newly created one
    # with a valid id assigned automatically
    assert product_list[-1][0] == last_id + 1
    assert product_list[-1][1] == 'тестові_дані'
    assert product_list[-1][2] == 'без_ід'

    # id in this test does not match usual test id (999)
    # defined in the Database class, and needs to be specified
    # for the successful teardown
    db.test_id = product_list[-1][0]


# ID 8
# check that NULL values can be successfully added as values
# for the name, description, and quantity columns of the products table
@pytest.mark.database
def test_null_values(db):
    # get list of all the products and save id of the last one
    product_list = db.get_all_products()
    last_id = product_list[-1][0]

    # add product with NULL quantity and no id, name, or description
    qnt = 'NULL'
    db.null_values(qnt)

    # get list of all the products again
    product_list = db.get_all_products()

    # check that the last product on the table is a newly created one
    # with a valid id assigned automatically
    # and NULL values in the name, description, and quantity
    assert product_list[-1][0] == last_id + 1
    assert product_list[-1][1] is None
    assert product_list[-1][2] is None
    assert product_list[-1][3] is None

    # id in this test does not match usual test id (999)
    # defined in the Database class, and needs to be specified
    # for the successful teardown
    db.test_id = product_list[-1][0]


# ID 9
# check that max integer value can be added as a valid id
@pytest.mark.database
@pytest.mark.wip
def test_id_max_value(db):
    max_integer_id = 9223372036854775807
    name = 'тестові'
    desc = 'дані'
    qnt = 10

    db.insert_product(max_integer_id, name, desc, qnt)
    product = db.get_product(max_integer_id)

    assert product[0][1] == 'тестові'
    assert product[0][2] == 'дані'

    # id in this test does not match usual test id (999)
    # defined in the Database class, and needs to be specified
    # for the successful teardown
    db.test_id = max_integer_id


# ID 10
# check that using integer value greater than the max integer value for the id
# raises an IntegrityError error
@pytest.mark.database
def test_id_out_of_range(db):
    max_integer_id = 9223372036854775807
    name = 'тестові'
    desc = 'дані'
    qnt = 10

    with pytest.raises(IntegrityError) as error:
        db.insert_product(max_integer_id+1, name, desc, qnt)

    assert "datatype mismatch" in str(error.value)
    assert "IntegrityError" in str(error.type)

    # id in this test does not match usual test id (999)
    # defined in the Database class, and needs to be specified
    # for the successful teardown
    db.test_id = max_integer_id+1


# TOOLBOX (comment these tests before running the entire set!)

# when you have a hammer everything looks like a nail
# (make custom requests to look up anything you need while creating tests)

@pytest.mark.hammer
def test_hammer(db):
    query = "SELECT * FROM products"

    result = db.hammer(query)

    for line in result:
        print()
        for cell in line:
            print(f"{cell} type {type(cell)}")


# manually EVAPORATE your mistakes! and stray test data

@pytest.mark.evaporate
def test_EVAPORATE(db):
    to_delete = []

    for id in to_delete:
        query = f"DELETE FROM products WHERE id = {id}"
        db.hammer(query)
