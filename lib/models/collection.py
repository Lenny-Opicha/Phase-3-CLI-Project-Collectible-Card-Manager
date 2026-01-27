from lib.db.connection import get_connection

class Collection:
    def __init__(self, name, owner, id=None):
        self.id = id
        self.name = name
        self.owner = owner

    # ---------- Properties ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Collection name must be a non-empty string.")
        self._name = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Owner must be a non-empty string.")
        self._owner = value

    # ---------- ORM Methods ----------
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                "INSERT INTO collections (name, owner) VALUES (?, ?)",
                (self.name, self.owner)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE collections SET name = ?, owner = ? WHERE id = ?",
                (self.name, self.owner, self.id)
            )

        conn.commit()
        conn.close()
        return self

    def delete(self):
        if self.id is None:
            raise ValueError("Collection must be saved before it can be deleted.")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM collections WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    # ---------- Class Methods ----------
    @classmethod
    def create(cls, name, owner):
        collection = cls(name=name, owner=owner)
        return collection.save()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()

        rows = cursor.execute("SELECT * FROM collections").fetchall()
        conn.close()

        return [cls(id=row[0], name=row[1], owner=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()

        row = cursor.execute(
            "SELECT * FROM collections WHERE id = ?",
            (id,)
        ).fetchone()

        conn.close()

        return cls(id=row[0], name=row[1], owner=row[2]) if row else None
