#!/usr/bin/python3

import sys
import requests
import json

if len(sys.argv) != 2:
	print('Usage: %s <asinfo.txt>' % (sys.argv[0],))
	sys.exit(1)

asn = open(sys.argv[1], newline='').readlines()
asn = [i.rstrip().split('\t')[0] for i in asn]

for i in asn:
	print('Fetching %s ..' % (i,))
	try:
		open('%s.json' % (i,))
		continue
	except:
		pass
	data = requests.get('https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS%s' % (i,))
	data = data.json()['data']['prefixes']
	data = [i['prefix'] for i in data]
	with open('%s.json' % (i,), 'w') as f:
		f.write(json.dumps(data))

result = {}
for i in asn:
	data = json.load(open('%s.json' % (i,)))
	for prefix in data:
		result[prefix] = i

with open('ip2asn.json', 'w') as f:
	f.write(json.dumps(result))
