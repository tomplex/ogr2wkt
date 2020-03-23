
import click

from ogr2wkt.util import convert_to_wkt


@click.command()
def cli():
    pass


@cli.command()
@click.argument('input_file')
@click.argument('output_file')
def ogr2wkt(input_file, output_file):
    convert_to_wkt(input_file, output_file)
