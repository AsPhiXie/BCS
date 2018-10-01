sbox = {0: 0xc, 1: 0xa, 2: 0xd, 3: 3, 4: 0xe, 5: 0xb, 6: 0xf, 7: 7, 8: 8, 9: 9, 0xa: 1, 0xb: 5, 0xc: 0, 0xd: 2, 0xe: 4, 0xf: 6}

def initialisation(n):
    final = ""
    for i in n:
        final += ord(i)
    return final

def subCell(s):
    res = 0
    for i in range(16):
        res |= sbox[((s >> (4*i)) & 0xf)] << (4*i)
    return res

def shuffleCell(s):
    l = [0, 10, 5, 15, 14, 4, 11, 1, 9, 3, 12, 6, 7, 13, 2, 8]
    res = 0
    for i in range(16):
        res |= ((s >> (4*l[i])) & 0xf) << (4*i)
    return res

def mixColumn(s):
    res = 0
    for i in range(16):
        t = (s >> (16*i)) & 0xFFFF
        u = ((t >> 4)^(t >> 8)^(t >> 12)) & 0xf
        u |= ((t ^ (t >> 8) ^ (t >> 12)) & 0xf) << 4
        u |= ((t ^ (t >> 4) ^ (t >> 12)) & 0xf) << 8
        u |= ((t ^ (t >> 4) ^ (t >> 12)) & 0xf) << 12
        res |= u << (16*i)
    return res