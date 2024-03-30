# Binary Data(Struct Module Overview) 

# Package/Library
`Struct`

## Purpose
The `struct` module in Python is used for converting between Python values and C structs represented as Python bytes objects. This is particularly useful for handling binary data stored in files or coming in from network connections, among other sources.

## Usage
You use the `struct` module by defining a format string that specifies the layout of the binary data, and then you pass this format string along with the data to functions like `pack` to encode Python values into binary data, or `unpack` to decode binary data into Python values. The format string determines the size and alignment of the packed data, using pre-defined format characters that represent different C data types (e.g., `I` for an unsigned int, `s` for a string).
The `struct` module provides a way to work with packed binary data, which is very efficient in terms of storage and processing speed, especially when dealing with external systems or low-level networking where the protocol requires binary data.

## Functionalities

### Packing Data: `struct.pack(format, v1, v2, ...)`
This function takes a format string and a sequence of values, packing the values into a bytes object according to the given format.
```
packed_data = struct.pack('!I5s', 7, b'Hello')
print(packed_data)
```
### Unpacking Data: `struct.unpack(format, buffer)`
This reverses the operation of `pack`, taking a bytes object and converting it back into a sequence of Python values.
```
unpacked_data = struct.unpack('!I5s', packed_data)
print(unpacked_data)

```
### Calculating Size: `struct.calcsize(format)` 
This function returns the size of the structure (in bytes) that would be created with the given format string, without actually packing any data.
```
size = struct.calcsize('!I5s')
print(size)

```
## Period of Creation
The `struct` module has been part of Python since its early versions, reflecting the language's design goal to be capable of interacting with C libraries and handling low-level data operations. Specific dates of creation or inclusion might vary, but it has been a staple in Python's standard library for decades.
