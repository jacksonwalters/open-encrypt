import numpy as np
from numpy.polynomial import polynomial as poly
from ring_lwe import parameters, polymul, polyadd, gen_binary_poly, gen_uniform_poly, gen_normal_poly
from sys import argv

def encrypt(pk, size, q, t, poly_mod, pt):
    """Encrypt an integer.
    Args:
        pk: public-key.
        size: size of polynomials.
        q: ciphertext modulus.
        t: plaintext modulus.
        poly_mod: polynomial modulus.
        pt: integer to be encrypted.
    Returns:
        Tuple representing a ciphertext.      
    """
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m  % q
    e1 = gen_normal_poly(size)
    e2 = gen_normal_poly(size)
    u = gen_binary_poly(size)
    ct0 = polyadd(
            polyadd(
                polymul(pk[0], u, q, poly_mod),
                e1, q, poly_mod),
            scaled_m, q, poly_mod
        )
    ct1 = polyadd(
            polymul(pk[1], u, q, poly_mod),
            e2, q, poly_mod
        )
    return (ct0, ct1)

#scheme's parameters
n, q, t, poly_mod = parameters()

if(len(argv) > 2):
    #get the public key from the string and format as two arrays
    pk_string = argv[1]
    pk_arr = [int(coeff) for coeff in pk_string.split(',')]
    pk_b = np.int64(pk_arr[:n])
    pk_a = np.int64(pk_arr[n:])
    pk = (pk_b,pk_a)
    #define the integers to be encrypted
    #note bytes are 8 bits, so message_int < 2^8 = t = plaintext modulus, which can be modified
    message = argv[2]
    message_bytes = [format(x, 'b') for x in bytearray(message, 'utf-8')]
    message_ints = [int(message_byte,2) for message_byte in message_bytes]
    #encrypt each integer message_int
    ciphertext_list = []
    for message_int in message_ints:
        ciphertext = encrypt(pk, n, q, t, poly_mod, message_int)
        ciphertext_list += ciphertext[0].tolist() + ciphertext[1].tolist()
    ciphertext_string = str(ciphertext_list).replace('[','').replace(']','').replace(' ','')
    print(ciphertext_string)