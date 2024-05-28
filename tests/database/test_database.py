import pytest
from modules.common.database import Database


@pytest.mark.database
@pytest.mark.wip
def test_database_connection():
    db = Database()
    db.test_connection()
