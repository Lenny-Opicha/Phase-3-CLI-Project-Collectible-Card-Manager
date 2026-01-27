from lib.db.connection import get_connection

class Card:
    VALID_RARITIES = ["common", "rare", "epic"]

    def __init__(self, name, rarity, collection_id, id=None):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.collection_id = collection_id

    # ---------- Properties ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Card name must be a non-empty string.")
        self._name = value

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        if value not in self.VALID_RARITIES:
            raise ValueError(
                f"Rarity must be one of: {', '.join(self.VALID_RARITIES)}"
            )
        self._rarity = value

    @property
    def collection_id(self):
        return self._collection_id

    @collection_id.setter
    def collection_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Collection ID must be an integer.")
        self._collection_id = value

    # ---------- ORM Methods ----------
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                """
                INSERT INTO cards (name, rarity, collection_id)
                VALUES (?, ?, ?)
                """,
                (self.name, self.rarity, self.collection_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                """
                UPDATE cards
                SET name = ?, rarity = ?, collection_id = ?
                WHERE id = ?
                """,
                (self.name, self.rarity, self.collection_id, self.id)
            )

        conn.commit()
        conn.close()
        return self

    def delete(self):
        if self.id is None:
            raise ValueError("Card must be saved before it can be deleted.")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM cards WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    # ---------- Class Methods ----------
    @classmethod
    def create(cls, name, rarity, collection_id):
        card = cls(name=name, rarity=rarity, collection_id=collection_id)
        return card.save()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()

        rows = cursor.execute("SELECT * FROM cards").fetchall()
        conn.close()

        return [
            cls(id=row[0], name=row[1], rarity=row[2], collection_id=row[3])
            for row in rows
        ]

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()

        row = cursor.execute(
            "SELECT * FROM cards WHERE id = ?",
            (id,)
        ).fetchone()

        conn.close()

        return (
            cls(id=row[0], name=row[1], rarity=row[2], collection_id=row[3])
            if row else None
        )

    @classmethod
    def find_by_collection(cls, collection_id):
        conn = get_connection()
        cursor = conn.cursor()

        rows = cursor.execute(
            "SELECT * FROM cards WHERE collection_id = ?",
            (collection_id,)
        ).fetchall()

        conn.close()

        return [
            cls(id=row[0], name=row[1], rarity=row[2], collection_id=row[3])
            for row in rows
        ]
