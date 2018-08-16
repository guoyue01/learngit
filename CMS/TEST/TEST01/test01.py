import os
'''
读取数据，写入数据
容错
'''

man=[]
other=[]

try:
    os.chdir('/Users/guoyue/PycharmProjects/CMS/TEST/DATA')
    data = open('testOpen')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'man':
                man.append(line_spoken)
            else:
                other.append(line_spoken)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')

        except ValueError:
            pass
    data.close()
except IOError:
    print('the datafile is missing')

try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('file error')

finally:
    man_file.close()
    other_file.close()


