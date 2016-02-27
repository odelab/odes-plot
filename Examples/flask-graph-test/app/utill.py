import hashlib

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


    
