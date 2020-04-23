def get_user_list(data_file, target_file):
    """function definition"""
    try:
        list_of_users = []

        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login)

        list_of_users.sort()
        line_no = 1

        fw = open(target_file, 'a')

        for user in list_of_users:
            content = '{:>6}  {}'.format(line_no, user)   # string formatting, :fmt-str
            print(content)
            fw.write(content + '\n')
            line_no += 1

        fw.close()

    except (FileNotFoundError, IOError) as error:
        print(error)


get_user_list('passwd.txt', 'passwd.dat')  # function call
