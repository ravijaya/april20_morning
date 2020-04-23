from json import load
from pyexcel import save_as
from pprint import pprint as pp


def read_json(json_file):
    """list of list form the json"""
    content = load(open(json_file))
    data_set = [['login', 'password', 'uid', 'gid', 'gecos', 'home', 'shell']]

    for login, user_info in content.items():
        temp = [login]
        temp.extend(list(user_info.values()))
        data_set.append(temp)

    return data_set


def json2xlsx(json_file, spreadsheet_name):
    data = read_json(json_file)
    save_as(dest_file_name=spreadsheet_name, array=data)


json2xlsx('passwd.json', 'passwd.xlsx')
