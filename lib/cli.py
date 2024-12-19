
import click
from models.user import create_user, update_user, delete_user
from models.activity import log_activity, update_activity, delete_activity
from models.emission_log import log_emission, update_emission, delete_emission

@click.group()
def cli():
    """CarbonTrack CLI - Track your carbon footprint."""
    pass

@cli.command()
@click.argument('name')
@click.argument('email')
@click.argument('location')
def create_user_command(name, email, location):
    """Create a new user."""
    user = create_user(name, email, location)
    if user:
        click.echo(f"User created: {user}")
    else:
        click.echo("Failed to create user.")

@cli.command()
@click.argument('user_id', type=int)
@click.argument('name', required=False)
@click.argument('email', required=False)
@click.argument('location', required=False)
def update_user_command(user_id, name, email, location):
    """Update user details."""
    user = update_user(user_id, name, email, location)
    if user:
        click.echo(f"User updated: {user}")
    else:
        click.echo("Failed to update user.")

@cli.command()
@click.argument('user_id', type=int)
def delete_user_command(user_id):
    """Delete a user."""
    if delete_user(user_id):
        click.echo(f"User with ID {user_id} deleted.")
    else:
        click.echo("Failed to delete user.")

@cli.command()
@click.argument('name')
@click.argument('emission_factor', type=float)
def create_activity_command(name, emission_factor):
    """Create a new activity."""
    activity = log_activity(name, emission_factor)
    if activity:
        click.echo(f"Activity created: {activity}")
    else:
        click.echo("Failed to create activity.")

@cli.command()
@click.argument('activity_id', type=int)
@click.argument('name', required=False)
@click.argument('emission_factor', type=float, required=False)
def update_activity_command(activity_id, name, emission_factor):
    """Update activity details."""
    activity = update_activity(activity_id, name, emission_factor)
    if activity:
        click.echo(f"Activity updated: {activity}")
    else:
        click.echo("Failed to update activity.")

@cli.command()
@click.argument('activity_id', type=int)
def delete_activity_command(activity_id):
    """Delete an activity."""
    if delete_activity(activity_id):
        click.echo(f"Activity with ID {activity_id} deleted.")
    else:
        click.echo("Failed to delete activity.")

@cli.command()
@click.argument('user_id', type=int)
@click.argument('activity_id', type=int)
@click.argument('duration', type=int)
@click.argument('date')
@click.argument('emissions', type=float)
def log_emission_command(user_id, activity_id, duration, date, emissions):
    """Log a new emission record."""
    emission = log_emission(user_id, activity_id, duration, date, emissions)
    if emission:
        click.echo(f"Emission logged: {emission}")
    else:
        click.echo("Failed to log emission.")

@cli.command()
@click.argument('emission_log_id', type=int)
@click.argument('emissions', type=float, required=False)
@click.argument('duration', type=int, required=False)
def update_emission_command(emission_log_id, emissions, duration):
    """Update an emission log."""
    emission = update_emission(emission_log_id, emissions, duration)
    if emission:
        click.echo(f"Emission updated: {emission}")
    else:
        click.echo("Failed to update emission.")

@cli.command()
@click.argument('emission_log_id', type=int)
def delete_emission_command(emission_log_id):
    """Delete an emission log."""
    if delete_emission(emission_log_id):
        click.echo(f"Emission log with ID {emission_log_id} deleted.")
    else:
        click.echo("Failed to delete emission log.")

if __name__ == '__main__':
    cli()

