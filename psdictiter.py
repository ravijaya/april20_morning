info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info.items())
print()

# iterate a dict for its (key, value) pair
for key, value in info.items():
    print(key, '->', value)