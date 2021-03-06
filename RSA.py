import random

def exponentiation(a,n,mod):
    if n == 1 :
        return a
    elif n%2 == 0:
        return (exponentiation(a**2, n/2, mod) % mod)
    elif (n > 2) & (n%2 != 0):
        return (a * exponentiation(a**2, (n-1)/2, mod) % mod)

def encrypt(plain,e,N):
    tab = []
    for a in plain:
        tab.append(exponentiation(ord(a),e,N))
    return tab

def PGCD(a,b):
    if b == 0:
        return a
    else:
        tmp = a%b
        return PGCD(b, tmp)

def GCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = GCD(b % a, a)
        return (g, x - (b // a) * y, y)

def inverse_modulaire(a, m):
    g, x, y = GCD(a, m)
    if g != 1:
        raise Exception('Pas d\'inversion modulaire existante')
    else:
        return x % m

def gen_prim(): #n = nombre de bit
    p = random.randint((2**2046), (2**2047))
    if (1 == ((2**(p-1))%p) == ((3**(p-1))%p) == ((5**(p-1))%p) == ((7**(p-1))%p)):
        return p
    else:
        return gen_prim()

def gen_e(p,q):
    psy = (p-1) * (q-1)
    for i in range(2,psy):
        if(PGCD(i, psy) == 1):
            return i

def decrypt(c, d, N):
    result = ""
    for i in c:
        result += chr(exponentiation(i,d,N))
    return result

def main():
    p = gen_prim()
    q = gen_prim()
    e = gen_e(p,q)
    msg = "test un deux un deux ici la terre"
    psy = (p-1)*(q-1)
    d = inverse_modulaire(e,psy)
    print("p = " + str(p))
    print("q = " + str(q))
    print("e = " + str(e))
    print("d = " + str(d))
    enc = encrypt(msg, e, (p*q))
    dec = decrypt(enc, d, (p*q))
    print("Chiffré par bloc = " + str(enc))
    print("Déchiffré = " + str(dec))

print(main())
