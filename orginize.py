from datetime import datetime
import os
import sys

src_address = sys.argv[1]
dest_address = sys.argv[2]


def copy_file(src_file_address, dest_file_address):
    with open(src_file_address, 'rb') as a:
        data = a.read()
        with open(dest_file_address, 'wb') as b:
            b.write(data)


def is_photo(file_name):
    photos_extensions = ['jpg', 'jpeg', 'png']
    parts = file_name.split('.')
    if len(parts) < 2:
        return False
    else:
        #  note the lower() function. file extension may be for example 'PNG'
        extension = parts[-1].lower()
    return extension in photos_extensions


def is_video(file_name):
    videos_extensions = ['mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov']
    parts = file_name.split('.')
    if len(parts) < 2:
        return False
    else:
        #  note the lower() function. file extension may be for example 'AVI'
        extension = parts[-1].lower()
        return extension in videos_extensions


def get_year_from_timestamp(timestamp):
    python_date = datetime.fromtimestamp(timestamp)
    return python_date.year


walk_result = os.walk(src_address)

for base_address, directory_names, file_names in walk_result:

    #  iterates through each file int the current directory
    for file_name in file_names:
        file_address = base_address + '/' + file_name

        modification_date = os.path.getmtime(file_address)
        file_year = get_year_from_timestamp(modification_date)

        if is_photo(file_name):
            file_dest_address = dest_address + '/' + str(file_year) + '/photos/'
        elif is_video(file_name):
            file_dest_address = dest_address + '/' + str(file_year) + '/videos/'
        else:
            file_dest_address = ''

        if file_dest_address != '':
            if not os.path.exists(file_dest_address):
                # this functions will create all directories recursively
                os.makedirs(file_dest_address)

            copy_file(file_address, file_dest_address + file_name)
