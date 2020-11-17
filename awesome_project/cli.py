#!/usr/bin/env python

# Third party modules
import click

# First party modules
import awesome_project


@click.group()
@click.version_option(version=awesome_project.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
