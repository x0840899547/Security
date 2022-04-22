import hashlib

path = r'C:\Users\Admin\Desktop\3Y2S\ComputerSec\Project'

with open(path, 'rb') as opened_file:
    content = opened_file.read()
    sha1 = hashlib.sha1()

    sha1.update(content)
    print('Result')
    print()
    print('{}: {}'.format(sha1.name,sha1.hexdigest()))