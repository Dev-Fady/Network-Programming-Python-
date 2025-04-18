b=bytes([0,1,98,99,100])
print(len(b))
print(b)
print(bytes('fady emil ','ascii'))

import struct
print(struct.pack('<i',4253))
print(struct.pack('>i',4253))