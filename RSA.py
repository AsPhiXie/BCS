import random

def exponentiation(a,n,mod):
    if n == 1 :
        return a
    elif n%2 == 0:
        return (exponentiation(a**2, n/2, mod) % mod)
    elif (n > 2) & (n%2 != 0):
        return (a * exponentiation(a**2, (n-1)/2, mod) % mod)

def encrypt(plain,e,N):
    result = ""
    for a in plain:
        result += str(exponentiation(ord(a),e,N))
    return result

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
    p = random.randint((2**10), (2**11))

    if (1 == ((2**(p-1))%p) == ((3**(p-1))%p) == ((5**(p-1))%p) == ((7**(p-1))%p)):
        return p
    else:
        return gen_prim()

print(encrypt("BONJOUR", 7, 5141))
print(PGCD(56,42))
print(inverse_modulaire(7,34))
print(gen_prim())