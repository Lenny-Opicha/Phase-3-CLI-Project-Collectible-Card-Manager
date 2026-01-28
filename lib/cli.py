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

    for c in collections:
        click.echo(f"{c.id}: {c.name} — {c.description}")


@cli.command("list-cards")
@click.argument("collection_id", type=int)
def list_cards(collection_id):
    """List cards in a collection"""
    cards = Card.find_by_collection(collection_id)
    if not cards:
        click.echo("No cards found.")
        return

    for card in cards:
        click.echo(f"{card.id}: {card.name} ({card.rarity})")


if __name__ == "__main__":
    cli()