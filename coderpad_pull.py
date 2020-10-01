import requests
import json
import click
from typing import List, Dict


def make_request(_url: str, _headers: Dict[str, str]) -> List[Dict[str, any]]:
    response = requests.get(_url, headers=_headers)
    if response.status_code is 200:
        data = json.loads(response.content)
        next_page = data.get('next_page')
        _pads = data.get('pads')
        if next_page is not None:
            print(f'retrieving next 50  at {next_page}')
            _pads = _pads + make_request(next_page, _headers)

        return _pads

    return []


@click.command()
@click.option('--file', default='pads_raw.json',
              help='Name of the file to dump the pads information into')
@click.argument('key')
def fetch(file, key: str) -> None:
    """
        Script to pull pads from Coderpad using the API token provided\n
        KEY: Coderpad API key to use
    """
    headers = {'Authorization': f'Token {key}'}
    # url = 'https://coderpad.io/api/pads?sort=updated_at,desc'  # personal pads
    url = 'https://coderpad.io//api/organization/pads'  # organizational pads
    pads = make_request(url, headers)

    with open(file, 'w') as outfile:
        json.dump(pads, outfile)
