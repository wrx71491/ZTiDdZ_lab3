import base64

def encode_string(mytext):
    text = mytext
    inbytes = base64.b64encode(bytes(text, 'utf-8'))
    encoded = inbytes.decode('utf-8')
    return encoded
    
def decode_string(mytext):
    text = mytext
    inbytes = base64.b64decode(bytes(text, 'utf-8'))
    encoded = inbytes.decode('utf-8')
    return encoded


if __name__ == '__main__':
    to_encode = input('Text do zakodwania:' )
    to_print = encode_string(to_encode)
    print(to_print)
    print(decode_string(to_print))
