#!/usr/bin/python3

import sys
import requests
import json
from multiprocessing import Pool

url = r'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS%s'


def work(asn):
	print('Fetching %s ..' % (asn,))
	try:
		open('%s.json' % (asn,))
		return
	except:
		pass

	data = requests.get(url % (asn,))
	data = data.json()['data']['prefixes']
	data = [i['prefix'] for i in data if i['prefix'] != '0.0.0.0/0' and i['prefix'] != '::/0']
	with open('%s.json' % (asn,), 'w') as f:
		f.write(json.dumps(data))


if len(sys.argv) < 2 or len(sys.argv) > 3:
	print('Usage: %s <asinfo.txt> [nproc]' % (sys.argv[0],))
	sys.exit(1)

asn = open(sys.argv[1], newline='').readlines()
asn = [i.rstrip().split('\t')[0] for i in asn]

try:
	nproc = int(sys.argv[2])
except IndexError:
	nproc = 4

with Pool(processes=nproc) as pool:
	pool.map(work, asn)

result = {}
for i in asn:
	data = json.load(open('%s.json' % (i,)))
	for prefix in data:
		result[prefix] = i

with open('ip2asn.json', 'w') as f:
	f.write(json.dumps(result))
