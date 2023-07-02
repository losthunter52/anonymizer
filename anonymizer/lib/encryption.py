import cryptocode
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import binascii

def encript_data(
    data,
    method = 'cryptocode'
):

    if method == 'cryptocode':
        cryptocode_method(data)

    if method == 'aes256':
        aes256_method(data)

    return data


def cryptocode_method(data):
    database = data.get_database()
    fields = data.get_fields()
    key = str(Random.get_random_bytes(32))
    
    for i in range(len(database)):
        for field in fields:
            database[i][field] = cryptocode.encrypt(database[i][field], key)

    data.update_database(database)
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("Cryptocode Key:")
    data.log.add_key(key)

    return data

def aes256_method(data):
    database = data.get_database()
    fields = data.get_fields()

    key = Random.get_random_bytes(32)
    iv = Random.new().read(AES.block_size)
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    for i in range(len(database)):
        for field in fields:
            aux = str.encode(database[i][field])
            database[i][field] = str(aes.encrypt(aux))

    data.update_database(database)
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("AES256 Key:")
    data.log.add_key(str(key))
    data.log.add_key("AES256 IV:")
    data.log.add_key(str(iv))
    
    return data