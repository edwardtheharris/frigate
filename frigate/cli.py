"""Frigate CLI module."""
import click
import frigate.gen
import frigate.pre_commit_hook
from frigate.utils import list_templates


@click.group()
def cli():
    """Run the command from the CLI."""



@cli.command()
@click.argument("filename")
@click.option(
    "-o",
    "--output-format",
    "output_format",
    default="markdown",
    help="Output format for the documentation",
    type=click.Choice(list_templates()),
)
@click.option(
    "--no-credits", is_flag=True, default=True, help="Disable the Frigate credits",
)
@click.option(
    "--no-deps", is_flag=True, default=True, help="Do not render dependency values",
)
def gen(filename, output_format, no_credits, no_deps):
    """Generate a frigate document.

    Args:
        filename ([type]): [description]
        output_format ([type]): [description]
        no_credits ([type]): [description]
        no_deps ([type]): [description]
    """
    click.echo(
        frigate.gen.gen(filename, output_format, credits=no_credits, deps=no_deps)
    )


@cli.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.option(
    "--artifact",
    default="README.md",
    help="What file to save the documentation as",
)
@click.option(
    "-o",
    "--output-format",
    "output_format",
    default="markdown",
    help="Output format for the documentation",
    type=click.Choice(list_templates()),
)
@click.option(
    "--no-credits",
    is_flag=True,
    default=True,
    help="Disable the Frigate credits",
)
@click.option(
    "--no-deps",
    is_flag=True,
    default=True,
    help="Do not render dependency values",
)
def hook(artifact, output_format, no_credits, no_deps):
    """Run the pre-commit hook.

    Args:
        artifact ([type]): [description]
        output_format ([type]): [description]
        no_credits ([type]): [description]
        no_deps ([type]): [description]
    """
    frigate.pre_commit_hook.main(artifact, output_format, credits=no_credits, deps=no_deps)
