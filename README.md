# open-encrypt
Full-stack encrypted messaging application using lattice-based methods in Python + PHP + SQL.

**NOTE**: This is a demo for educational purposes only. It is not meant for real-world use.

**ENCRYPTION METHODS**: ring-LWE, module-LWE

**RESOURCES**:

- ring-LWE in Python: https://blog.openmined.org/build-an-homomorphic-encryption-scheme-from-scratch-with-python/
- module-LWE in Python: https://cryptographycaffe.sandboxaq.com/posts/kyber-01/
- ring-LWE notes: https://math.colorado.edu/~kstange/teaching-resources/crypto/RingLWE-notes.pdf
- NIST Post-Quantum: https://csrc.nist.gov/projects/post-quantum-cryptography
- Red Hat Post-Quantum/Lattices: https://www.redhat.com/en/blog/post-quantum-cryptography-lattice-based-cryptography
- Latticed-based cryptography: https://thelatticeclub.com

---

**SQL**: 

Three tables are required to store login_info, messages, and public_keys.

_login_info_:
  - username CHAR(14)
  - password CHAR(60)
  - token CHAR(32)

Passwords are hashed using standard hashing. Secure, random tokens stored for user sessions.

_messages_:
  - from CHAR(14)
  - to CHAR(14)
  - message VARCHAR(8000)

Messages are stored encrypted. The inflation ratio is ~13.7.

_public_keys_:
  - username CHAR(14)
  - public_key CHAR(192)

Public keys are a single string representing two (reduced cyclotomic) polynomials which are each arrays of `int`s.

**PHP**:

Used to handle basic account creation, login, and SQL insertions/lookups. 

**Python**:

Python scripts are executed directly using `shell_exec`. Output is printed and passed back as a string.
  
