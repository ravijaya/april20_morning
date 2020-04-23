info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info)
print()

item = 'version'

if item in info:  # validate for the key
    info[item] = 3.4  # update

print(info)
print()

info['arch'] = 'x86_64'# add an element
print(info)
print()


@ 11:30 AM