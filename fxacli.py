import random
import string

import click
import crayons
from fxa.core import Client
from fxa.constants import ENVIRONMENT_URLS
from fxa.tests.utils import TestEmailAccount


@click.group()
@click.option('--env', type=click.Choice(['production', 'stage', 'stable']),
              default='stage', help='Firefox Account environment.')
@click.pass_context
def cli(ctx, env):
    ctx.obj['URL'] = ENVIRONMENT_URLS[env]['authentication']


@cli.command()
@click.pass_context
def create(ctx):
    """Create a Firefox Account."""
    account = TestEmailAccount()
    client = Client(ctx.obj['URL'])
    password = ''.join([random.choice(string.ascii_letters) for i in range(8)])
    session = client.create_account(account.email, password)
    click.echo('Account {}!\n - 🌐  {}\n - 📧  {}\n - 🔑  {}'.format(
        crayons.yellow('created'), ctx.obj['URL'], account.email, password))
    message = account.wait_for_email(lambda m: 'x-verify-code' in m['headers'])
    session.verify_email_code(message['headers']['x-verify-code'])
    click.echo('Account {}! 🎉'.format(crayons.green('verified')))
    account.clear()


@cli.command()
@click.argument('email')
@click.argument('password')
@click.pass_context
def destroy(ctx, email, password):
    """Destroy a Firefox Account."""
    client = Client(ctx.obj['URL'])
    client.destroy_account(email, password)
    click.echo('Account {}! 💥'.format(crayons.red('destroyed')))


cli.add_command(create)
cli.add_command(destroy)


if __name__ == '__main__':
    cli(obj={})
