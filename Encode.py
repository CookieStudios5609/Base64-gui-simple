import base64

inputmsg = 'Your Text Here'
message_bytes = inputmsg.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
inputenc = base64_bytes.decode('ascii')

print(inputenc)