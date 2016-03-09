import hashlib, os, shutil

def hashFileName(fileName):
    """ return a hashed file name with the same extension, assuming there is
        one

        Algorithm: SHA256
    """
    # notice that 'xx.txt' and 'xx' will get different hashes
    byte_name = bytes(fileName)
    hash_object = hashlib.sha256(byte_name)
    hex_dig = hash_object.hexdigest()
    new_name = hex_dig
    # get the extension
    dot_index = fileName.find('.')
    if dot_index != -1:
        extension = fileName[dot_index:]
        new_name = new_name + extension

    return new_name

def deleteDirectoryFiles(folder):
    """ delete all the files and subdirectories in one folder
        directory input should be an absolute path
    """
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e

def listIterableContents(iterable):
    result = ''
    for each in iterable:
        result += ' ' + str(each)
    return result

