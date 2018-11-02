import json
import random
import string

import click
import crayons
from fxa.constants import ENVIRONMENT_URLS
from fxa.core import Client
from fxa.errors import ClientError
from fxa.tests.utils import TestEmailAccount

DATA_FILENAME = ".accounts"


@click.group()
@click.option(
    "--env",
    type=click.Choice(ENVIRONMENT_URLS.keys()),
    default="stage",
    help="Firefox Account environment.",
)
@click.pass_context
def cli(ctx, env):
    ctx.obj = {}
    ctx.obj["URL"] = ENVIRONMENT_URLS[env]["authentication"]


@cli.command()
@click.pass_context
def create(ctx):
    """Create a Firefox Account."""
    account = TestEmailAccount()
    client = Client(ctx.obj["URL"])
    password = "".join([random.choice(string.ascii_letters) for i in range(8)])
    session = client.create_account(account.email, password)
    add(ctx.obj["URL"], account.email, password)
    click.echo(
        "Account {}!\n{}".format(
            crayons.yellow("created"), render(ctx.obj["URL"], account.email, password)
        )
    )
    message = account.wait_for_email(lambda m: "x-verify-code" in m["headers"])
    session.verify_email_code(message["headers"]["x-verify-code"])
    click.echo("Account {}! 🎉".format(crayons.green("verified")))
    account.clear()


@cli.command()
@click.option("--all", "_all", is_flag=True, help="Destroy all known accounts")
@click.option("--email", help="Email address of Firefox Account user")
@click.option("--password", help="Password of Firefox Account user")
@click.pass_context
def destroy(ctx, _all, email, password):
    """Destroy a Firefox Account."""
    accounts = []
    stored = load()

    try:
        if email and password:
            account = {"url": ctx.obj["URL"], "email": email, "password": password}
            accounts.append(account)
            stored.remove(account)
        elif email:
            click.echo("You must specify a {}! 🔑".format(crayons.magenta("--password")))
            exit(1)
        else:
            if _all and stored:
                accounts.extend(stored)
                stored = []
            else:
                accounts.append(stored.pop())
    except ValueError:
        pass  # account unknown to .accounts
    except IndexError:
        click.echo("No account to destroy! 🎻")
        exit(1)

    for account in accounts:
        client = Client(account["url"])
        try:
            client.destroy_account(account["email"], account["password"])
            click.echo(
                "Account {}! 💥\n{}".format(
                    crayons.red("destroyed"),
                    render(account["url"], account["email"], account["password"]),
                )
            )
        except ClientError as e:
            if e.errno == 102:
                click.echo(
                    "Account {}! 🔍\n{}".format(
                        crayons.cyan("unknown"),
                        render(account["url"], account["email"], account["password"]),
                    )
                )
            else:
                raise

    save(stored)


def render(url, email, password):
    return f" - 🌐  {url}\n - 📧  {email}\n - 🔑  {password}"


def load():
    try:
        with open(DATA_FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add(url, email, password):
    accounts = load()
    accounts.append({"url": url, "email": email, "password": password})
    save(accounts)


def save(accounts):
    with open(DATA_FILENAME, mode="w") as f:
        json.dump(accounts, f, indent=2)


cli.add_command(create)
cli.add_command(destroy)


if __name__ == "__main__":
    cli()
