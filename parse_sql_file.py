from pathlib import Path
import re

path = Path('/Users/jwt/Library/Containers/com.ootpdevelopments.ootp23macqlm/Data/Application Support/Out of the Park Developments/OOTP Baseball 23/saved_games/NYMETS QS.lg/import_export/mysql')
# load all files in the directory into a list
files = path.glob('*.*')
# sort the list
files = sorted(files)
# create file to hold the schema
with open('/Users/jwt/PycharmProjects/cpi/schema.sql', 'w') as schema:
    schema.write('# Schema for OOTP 2023 \n')


insert = re.compile(r"\s(insert)")
# match last hashtag in a string
last_hashtag = re.compile(r"\# \n(?=[^#]*$)")

# print the list

for file in files:

# open the file
    file_name = str.split(file.name, '.')[0]
    f = open(file, 'r')
    # read the file
    data = f.read()
    match = insert.search(data)
    if match is None:
        continue
    else:
        sql_text = data[0:match.start()]
    match = last_hashtag.search(sql_text)
    sql_text = sql_text[match.end():]
    # write the file to the schema file
    with open('/Users/jwt/PycharmProjects/cpi/schema.sql', 'a') as schema:
        schema.write(f'-- {file_name}\n')
        schema.write(sql_text)
    # close the file
    f.close()


