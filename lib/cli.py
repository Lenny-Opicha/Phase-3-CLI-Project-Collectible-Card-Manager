import click
from lib.models.card import Card


@click.group()
def cli():
    """Collectible Card Manager CLI"""
    pass


@cli.command()
@click.argument("collection_id", type=int)
def list_cards(collection_id):
    """List all cards in a collection"""
    cards = Card.get_by_collection(collection_id)

    if not cards:
        click.echo("No cards found.")
        return

    for card in cards:
        click.echo(
            f"{card.id}: {card.name} ({card.rarity}) — Value: {card.estimated_value}"
        )


@cli.command()
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


@cli.command()
@click.argument("name")
def find_card(name):
    """Find cards by name"""
    cards = Card.find_by_name(name)

    if not cards:
        click.echo("No matching cards found.")
        return

    for card in cards:
        click.echo(
            f"{card.id}: {card.name} ({card.rarity}) — Value: {card.estimated_value}"
        )


@cli.command()
@click.argument("card_id", type=int)
def delete_card(card_id):
    """Delete a card by ID"""
    deleted = Card.delete(card_id)

    if deleted:
        click.echo(f"🗑️ Card {card_id} deleted successfully.")
    else:
        click.echo("Card not found.")


if __name__ == "__main__":
    cli()
