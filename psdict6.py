import pprint

info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

# lookup aka read
print(info['host'])
print(info['domain'])
# print(info['apps'])
print()


print(info.get('app'))
print(info.get('apps'))
print()

print(info.get('app', 'tomcat'))
print(info.get('apps', 'tomcat'))
print()

# if value:
#     print(value)
# else:
#     print('not a valid key')
