#!/usr/bin/python3.6

import sys
import requests
import json

from pprint import pprint

if len(sys.argv) != 2:
	print(f'Usage: {sys.argv[0]} <asinfo.txt>')
	sys.exit(1)

with open(sys.argv[1], 'r') as f:
	asn = f.readlines()
	asn = [i.rstrip().split('\t')[0] for i in asn]

for i in asn:
	print(f'Fetching {i}..')
	try:
		open(f'{i}.json', 'r')
		continue
	except:
		pass
	data = requests.get(f'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS{i}')
	data = data.json()['data']['prefixes']
	data = [i['prefix'] for i in data]
	with open(f'{i}.json', 'w') as f:
		f.write(json.dumps(data))

result = {}
for i in asn:
	with open(f'{i}.json', 'r') as f:
		data = f.readlines()
		data = [i.rstrip() for i in data]
	data = json.loads(data[0])
	for prefix in data:
		result[prefix] = i

with open('ip2asn.json', 'w') as f:
	f.write(json.dumps(result))

