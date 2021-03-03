import os

if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.exists('log/log_file.txt'):
    f = open('log/log_file.txt', 'w')
    f.write('start file')
    f.close()