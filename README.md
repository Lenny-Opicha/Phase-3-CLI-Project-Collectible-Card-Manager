Project Name : Collectible Card Manager
Description ;
A Python CLI application to manage collectible card collections using SQLite and Click.

Features
1. List and manage card collections
2. Add, list, update, delete cards
3. Search cards by name
4. Persistent storage with SQLite

How to operate it ?
```bash
python -m lib.cli list-collections
python -m lib.cli add-card 1
python -m lib.cli find-card pikachu
python -m lib.cli update-card 5
python -m lib.cli delete-card 5