info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info)
print()

value = info.pop('desc')
print(value)

del info['app']
print(info)
