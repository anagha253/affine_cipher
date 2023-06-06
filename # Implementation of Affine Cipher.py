# Implementation of Affine Cipher in Python

# Extended Euclidean Algorithm 
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None # modular inverse does not exist
	else:
		return x % m


# affine cipher encryption function

def encrypt(text, key):
	
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
				+ ord('A')) for t in text.upper().replace(' ', '') ])


# affine cipher decryption function

def decrypt(cipher, key):
	
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
					% 26) + ord('A')) for c in cipher ])



def main():
	
    txt=input("Enter the text to be encrypted:")
    a=int(input("Enter the key1:"))
    b=int(input("Enter the key2:"))
    key = [a,b]

    affine_encrypted_text = encrypt(txt, key)

    print('Encrypted Text: {}'.format( affine_encrypted_text ))

    print('Decrypted Text: {}'.format
	( decrypt(affine_encrypted_text, key) ))


if __name__ == '__main__':
	main()

