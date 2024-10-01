import os
from pathlib import Path
from sqlite3 import Connection, Cursor, connect

is_testing = bool(os.getenv("IS_TESTING", "False"))
conn: Connection | None = None
curs: Cursor | None = None

def init_db(db_name: str = "db.sqlite", reset: bool = False):
    global conn, curs
    if conn is not None:
        if not reset:
            return
        conn = None
    db_path = Path(__file__).resolve().parents[1] / "db" / db_name
    if is_testing:
        db_path = db_name

    conn = connect(db_path, check_same_thread=False)
    curs = conn.cursor()

init_db()
