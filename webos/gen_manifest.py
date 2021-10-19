#!/usr/bin/env python3
import argparse
import hashlib
import json
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--appinfo', required=True)
parser.add_argument('-p', '--pkgfile', required=True)
parser.add_argument('-o', '--output', required=True)

args = parser.parse_args()

outfile = args.output

with open(args.appinfo) as f:
    appinfo = json.load(f)

with open(args.pkgfile, 'rb') as f:
    hasher = hashlib.new('sha256')
    seglen = hasher.block_size * 0x800
    segment = f.read(seglen)
    while segment:
        hasher.update(segment)
        segment = f.read(seglen)

    pkghash = hasher.hexdigest()
    pkgfile = path.basename(args.pkgfile)

with open(outfile, 'w') as f:
    json.dump({
        'id': appinfo['id'],
        'version': appinfo['version'],
        'type': appinfo['type'],
        'title': appinfo['title'],
        'appDescription': appinfo['appDescription'],
        'iconUri': 'https://github.com/webosbrew/SpaceCadetPinball/raw/webos/webos/icon.png',
        'sourceUrl': 'https://github.com/webosbrew/SpaceCadetPinball',
        'rootRequired': False,
        'ipkUrl': pkgfile,
        'ipkHash': {
            'sha256': pkghash
        }
    }, f)
