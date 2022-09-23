# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os


def get_users(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()
    lines = filter(lambda x: x.strip(), lines)
    lines = [ll.rstrip('\n') for ll in lines]
    names = []
    for ll in lines:
        _, user = ll.split('https://ichbinhier-twittertools.herokuapp.com/blocklists?users=', 1)
        names.extend(user.split(','))
        # print(user.split(','))
        # break
    return names


def create_links(u_names):
    link_length = 4096
    li = 'https://ichbinhier-twittertools.herokuapp.com/blocklists?users='
    s_len = len(li)
    max_users_len = link_length - s_len
    links = []
    c_names = []
    c_len = 0
    for u in u_names:
        if c_len + len(u) + 1 < max_users_len:
            c_len += len(u) + 1
            c_names.append(u)
        else:
            u_string = ','.join(c_names)
            link = li + u_string
            links.append(link)
            c_names = []
            c_len = 0
    return links


def create_readme(links):
    clickable_link = []
    for idx, link in enumerate(links):
        r = f'[Link {idx}]({link})'
        clickable_link.append(r)
    with open("read.txt", 'w') as f:
        for lin in clickable_link:
            f.write(lin)
            f.write('\n\n')
    # [Link 1]()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users = get_users('raw_links.txt')
    u_links = create_links(users)
    # print(u_links)
    create_readme(u_links)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
