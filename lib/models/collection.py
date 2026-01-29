from lib.db import CURSOR, CONN


class Collection:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def create(cls, name, description):
        CURSOR.execute(
            "INSERT INTO collections (name, description) VALUES (?, ?)",
            (name, description)
        )
        CONN.commit()
        return cls.find_by_id(CURSOR.lastrowid)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM collections").fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute(
            "SELECT * FROM collections WHERE id = ?",
            (id,)
        ).fetchone()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        from lib.db import CURSOR, CONN
        CURSOR.execute("DELETE FROM collections WHERE id = ?", (id,))
        CONN.commit()