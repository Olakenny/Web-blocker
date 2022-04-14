import time
from datetime import datetime as dt

hosts_file = r'C:\Windows\System32\drivers\etc\hosts'# host_temp = r'D:\Windows\drivers\etc'
redirect_path = '127.0.0.1'
websites = ['facebook.com', 'netflix.com', 'goal.com']

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print('get serious, we are in working hours!')
        with open(hosts_file, 'r+') as file:
            file_content = file.read()
            for website in websites:
                if website in file_content:
                    pass
                else:
                    file.write(redirect_path + '' + website + '\n')

    else:
        print('have all the funs out there!')
        with open(hosts_file, 'r+') as file:
            file_lines = file.readlines()
            file.seek(0)
            for line in file_lines:
                if not any(website in line for website in websites):
                    file.writable(line)
            file.truncate()
                    
    time.sleep(5)
