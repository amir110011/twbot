import time

def new_twitt():
    # variable
    file_name = 'mytwitts.txt'
    new_twitts = ''
    tempdata = ''
    temp_list = []
    # logic
    with open(file_name, 'r+') as f:
        for i in f:
            tempdata += i
            if i == "*\n":
                temp_list.append(tempdata)
                tempdata = ''
    new_twitts = temp_list[0]
    new_twitts = new_twitts.replace('*\n', '')
    with open(file_name, 'w') as f:
        del temp_list[0]
        f.writelines(temp_list)
    return new_twitts


def logs(msg):
    with open('logs.txt', 'a+') as f:
        now = time.strftime("%Y-%m-%d %H:%M")
        f.write(f'$ {now}: {msg}\n')


