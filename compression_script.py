import shutil
import os
import datetime

def compression():
    # Gets file/folder for compression and required compression type
    path = input("Enter the path of the file/folder you wish to compress: ")
    compression_type = input("Enter the compression type (.zip, .tar, or .tgz): ")
    valid_types = {'.zip','.tar','.tgz'}

    # Checks for required compression type and performs compression
    if compression_type not in valid_types:
        print ("Invalid compression type, please try again!")
    else:
        base_name = os.path.basename(path)
        current_date = datetime.datetime.now().strftime("%d_%m_%Y")
        new_name = f'{base_name}_{current_date}{compression_type}'
        
        try:
            shutil.make_archive(new_name[:-4], compression_type[1:], path)
            print(f"Compression successful! Compressed file saved as: {new_name}")
        except Exception as e:
            print(f"Error during compression: {e}")
    
if __name__ == "__main__":
    compression()