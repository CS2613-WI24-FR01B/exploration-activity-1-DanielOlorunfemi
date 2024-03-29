import struct

def encode_text(text, encoding_schema='utf-8'):
    # Encode text to binary using UTF-8, then pack it with its length
    text_bytes = text.encode(encoding_schema)
    return struct.pack(f'!I{len(text_bytes)}s', len(text_bytes), text_bytes)

def decode_text(binary_data, encoding_schema='utf-8'):
    # Unpack the binary data to get text length and text
    length = struct.unpack('!I', binary_data[:4])[0]
    text = struct.unpack(f'!{length}s', binary_data[4:])[0]
    return text.decode(encoding_schema)

# Example usage
encoded_data = encode_text("AI World!")
print(f"Encoded Data: {encoded_data}")
decoded_text = decode_text(encoded_data)
print(f"Decoded Text: {decoded_text}")
