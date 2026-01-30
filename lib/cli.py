import click

from lib.models.collection import Collection
from lib.models.card import Card


@click.group()
def cli():
    """Collectible Card Manager CLI"""
    pass


@cli.command("list-collections")
def list_collections():
    """List all collections"""
    collections = Collection.get_all()
    if not collections:
        click.echo("No collections found.")
        return

    for collection in collections:
        click.echo(
            f"{collection.id}: {collection.name} — {collection.description}"
        )


@cli.command("add-collection")
def add_collection():
    """Add a new collection"""
    name = click.prompt("Collection name")
    description = click.prompt("Description")

    collection = Collection.create(name, description)
    click.echo(f"✅ Collection added with ID {collection.id}")


@cli.command("delete-collection")
@click.argument("collection_id", type=int)
def delete_collection(collection_id):
    """Delete a collection by ID"""
    success = Collection.delete(collection_id)

    if not success:
        click.echo("❌ Collection not found")
        return

    click.echo(f"🗑️ Collection {collection_id} deleted")


@cli.command("list-cards")
@click.argument("collection_id", type=int)
def list_cards(collection_id):
    """List cards in a collection"""
    cards = Card.get_by_collection(collection_id)

    if not cards:
        click.echo("No cards found for this collection.")
        return

    for card in cards:
        click.echo(
            f"{card.id}: {card.name} ({card.rarity}) — Value: {card.estimated_value}"
        )


@cli.command("add-card")
@click.argument("collection_id", type=int)
def add_card(collection_id):
    """Add a new card to a collection"""
    name = click.prompt("Card name")
    rarity = click.prompt("Rarity")
    estimated_value = click.prompt("Estimated value", type=float)

    card = Card.create(name, rarity, collection_id, estimated_value)

    click.echo(
        f"✅ Card added: {card.name} ({card.rarity}) — Value: {card.estimated_value}"
    )


if __name__ == "__main__":
    cli()
