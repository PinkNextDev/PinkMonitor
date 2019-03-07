
from monitor.db_manager import DBManager


# Puts blocks data to PostgreSQL db.
with DBManager() as db_manager:
    db_manager.update()
