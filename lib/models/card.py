from lib.db import CURSOR, CONN


class Card:
    def __init__(self, id, collection_id, name, rarity):
        self.id = id
        self.collection_id = collection_id
        self.name = name
        self.rarity = rarity

    @classmethod
    def create(cls, collection_id, name, rarity):
        CURSOR.execute(
            "INSERT INTO cards (collection_id, name, rarity) VALUES (?, ?, ?)",
            (collection_id, name, rarity)
        )
        CONN.commit()
        return cls.find_by_id(CURSOR.lastrowid)

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM cards").fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute(
            "SELECT * FROM cards WHERE id = ?",
            (id,)
        ).fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_collection(cls, collection_id):
        rows = CURSOR.execute(
            "SELECT * FROM cards WHERE collection_id = ?",
            (collection_id,)
        ).fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def delete(cls, id):
        CURSOR.execute("DELETE FROM cards WHERE id = ?", (id,))
        CONN.commit()