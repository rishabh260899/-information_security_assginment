def func1(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = func1(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
 
 
# affine cipher encryption function
def affine_encrypt(text, key):
   
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# affine cipher decryption function
def affine_decrypt(cipher, key):
   
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 

def main():
    
    text = 'java python'
    key = [17, 20]
 
    
    affine = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine ))
 
    
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine, key) ))
 
 
if __name__ == '__main__':
    main()
