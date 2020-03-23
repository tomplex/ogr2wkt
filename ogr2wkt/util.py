import csv
import sys
from itertools import chain
from typing import Dict, Iterable

import fiona

from geomet import wkt

csv.field_size_limit(sys.maxsize)


class wkt_dialect(csv.unix_dialect):
    delimiter = '|'
    quoting = csv.QUOTE_MINIMAL


def create_line(feature: Dict[str]) -> Iterable:
    return chain([feature['id']], map(str, feature['properties'].values()), [wkt.dumps(feature['geometry'])])


def list_fields(src: fiona.Collection) -> list:
    return list(chain(['id'], map(lambda n: n.lower(), src.schema['properties'].keys()), ['wkt']))


def convert_to_wkt(input_file, output_file):
    with fiona.open(input_file) as src, \
            open(output_file, 'w') as output_fobj:
        writer = csv.writer(output_fobj, dialect=wkt_dialect)
        writer.writerow(list_fields(src))

        for idx, feature in enumerate(src):
            writer.writerow(create_line(feature))
