def get_user_list(data_file):
    """function definition"""
    try:
        list_of_users = []

        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login)

        list_of_users.sort()
        line_no = 1

        for user in list_of_users:
            print('{:>6}  {}'.format(line_no, user))   # string formatting, :fmt-str
            line_no += 1

    except (FileNotFoundError, IOError) as error:
        print(error)


get_user_list('passwd.txt')  # function call
