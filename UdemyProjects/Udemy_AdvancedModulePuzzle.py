import shutil
import os
import re

pattern = r'\d{3}-\d{3}-\d{4}'


def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        pass


results = []

for folders, sub_folders, files in os.walk( 'C:\\Users\\josh5\\PycharmProjects\\Complete-Python-3-Bootcamp-master_USE THIS\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise' + '\\' + 'extracted_content'):

    for f in files:
        fullpath = folders + '\\' + f
        results.append(search(fullpath))

for r in results:
    if r != None:
        print(r.group())
