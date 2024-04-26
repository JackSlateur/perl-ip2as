#!/bin/sh

# Create free account at Maxmind via
# https://www.maxmind.com/en/geolite2/signup
# and generate License key

ACCOUNT="ACCOUNT_ID_HERE"
LICENSE="LICENSE_KEY_HERE"
DIR="./"

rm -f ${DIR}GeoLite2*.zip
rm -f ${DIR}GeoLite2*.csv

wget -q -4 -O${DIR}GeoLite2-ASN-CSV.zip "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN-CSV&license_key=${LICENSE}&suffix=zip"
unzip -q -j ${DIR}GeoLite2-ASN-CSV.zip */*.csv
tail -q -n +2 ${DIR}GeoLite2-ASN-Blocks-IPv4.csv ${DIR}GeoLite2-ASN-Blocks-IPv6.csv | jq -n -R '
inputs |
split(",") |
{ (.[0]):  .[1] } '  | jq -s add > ${DIR}ip2asn.json

rm -f ${DIR}GeoLite2*.zip
rm -f ${DIR}GeoLite2*.csv
