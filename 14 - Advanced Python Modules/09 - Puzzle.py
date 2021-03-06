import shutil
import re
import os
import pdb

# (shutil) Extract folders & files from zip file
zip_file = os.getcwd() +'/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/unzip_me_for_instructions.zip'
shutil.unpack_archive(zip_file, os.getcwd()+'/14 - Advanced Python Modules/', 'zip')

# (re) Check number pattern in texts by reading files
def check(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern, text):
        return re.search(pattern, text)

# (os) Find files and send to the search function
results = []
for folder , sub_folders , files in os.walk(os.getcwd()+'/14 - Advanced Python Modules/extracted_content'): 
    for f in files:
        full_path = folder+'/'+f
        results.append(check(full_path))

# pdb.set_trace()

# extract number 
for r in results:
    if r!= None:
        print(r.group())