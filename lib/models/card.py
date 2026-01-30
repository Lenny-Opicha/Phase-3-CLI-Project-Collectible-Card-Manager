from lib.db import CURSOR, CONN


class Card:
    def __init__(self, id, name, rarity, estimated_value, collection_id):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.estimated_value = estimated_value
        self.collection_id = collection_id

    @classmethod
    def create(cls, name, rarity, collection_id, estimated_value):
        CURSOR.execute(
            """
            INSERT INTO cards (name, rarity, estimated_value, collection_id)
            VALUES (?, ?, ?, ?)
            """,
            (name, rarity, estimated_value, collection_id),
        )
        CONN.commit()

        id = CURSOR.lastrowid
        return cls(id, name, rarity, estimated_value, collection_id)

    @classmethod
    def get_by_collection(cls, collection_id):
        rows = CURSOR.execute(
            """
            SELECT id, name, rarity, estimated_value, collection_id
            FROM cards
            WHERE collection_id = ?
            """,
            (collection_id,),
        ).fetchall()

        return [cls(*row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        rows = CURSOR.execute(
            """
            SELECT id, name, rarity, estimated_value, collection_id
            FROM cards
            WHERE name LIKE ?
            """,
            (f"%{name}%",),
        ).fetchall()

        return [cls(*row) for row in rows]

    @classmethod
    def delete(cls, card_id):
        CURSOR.execute("DELETE FROM cards WHERE id = ?", (card_id,))
        CONN.commit()
        return CURSOR.rowcount

    @classmethod
    def update(cls, card_id, name, rarity, estimated_value):
        CURSOR.execute(
            """
            UPDATE cards
            SET name = ?, rarity = ?, estimated_value = ?
            WHERE id = ?
            """,
            (name, rarity, estimated_value, card_id),
        )
        CONN.commit()