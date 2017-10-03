What is ip2as
===

ip2as is a small perl module to help map IP adresses to ASN. Both IP version are supported transparently.

Prerequisites
---

 - Perl (5.14 required)
 - libnet-patricia-perl
 - libjson-xs-perl (optional, you should use it)

How to use
---

 - First, create a json with a list of prefix -> ASN. tools/ip2asn.json is provided full a snapshot of the current internet view.
 - Load the json:
```perl
ip2as::init('path/to/mapping.json');
```
 - Do some queries:
```perl
print ip2as::getas4ip('8.8.8.8'); #prints 15169
print ip2as::getas4ip('2001:4f8:1:10:0:1991:8:25'); #prints 1280
```
 - When nothing is found, getas4ip returns undef.

Known bugs
---

This is not really a code-bug, but the default file contains stupid data due to misinformation from the RIPE (and some bad folks):
```perl
print ip2as::getas4ip('::') . "\n"; #prints 29049
print ip2as::getas4ip('10.0.0.1') . "\n"; #prints 15576
```

That specific issue is now fixed (by static exclusion), it remains sensitive to bad data.
