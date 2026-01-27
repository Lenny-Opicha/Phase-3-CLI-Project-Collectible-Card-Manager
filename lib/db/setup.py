from .connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS collections (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            owner TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            rarity TEXT NOT NULL,
            collection_id INTEGER NOT NULL,
            FOREIGN KEY (collection_id) REFERENCES collections(id)
        )
        """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
