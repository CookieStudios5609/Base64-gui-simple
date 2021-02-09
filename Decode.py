import base64

encoded = 'c3V1dXVwcHBwb3I=='  # encoded here, very cool
base64_bytes = encoded.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
decoded = message_bytes.decode('ascii')

print(decoded)