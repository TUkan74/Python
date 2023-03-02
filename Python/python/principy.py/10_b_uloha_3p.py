# jednoduchy list, kde kazda cast listu je iny priklad


x = [0]*9
x[0] = 0x51 | 3
x[1] = 0x7F02 | 0x8E18
x[2] = 256 | 0x00FF
x[3] = 0xF0005090 | 0x01F3080B
x[4] = 0xFFFF & 256
x[5] = 0x1234 & 0x0200
x[6] = 0xC9815093 & 0x00004000
x[7] = 0xC9815093 & 0xFFFEFFFF
x[8] = 0xC9815093 ^ 0xFF000000

# pomocou for loopu vypiseme

for i in range(len(x)):
    print("x [",i,"] = ",hex(x[i]))

# vyjde nam
    ''' 
x [ 0 ] =  0x53
x [ 1 ] =  0xff1a
x [ 2 ] =  0x1ff
x [ 3 ] =  0xf1f3589b
x [ 4 ] =  0x100
x [ 5 ] =  0x200
x [ 6 ] =  0x4000
x [ 7 ] =  0xc9805093
x [ 8 ] =  0x36815093
    '''