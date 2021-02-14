import base64

encoded = 'WW91ciBUZXh0IEhlcmU='  # encoded here, very cool
base64_bytes = encoded.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
decoded = message_bytes.decode('ascii')

print(decoded)
