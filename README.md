# open-encrypt
Full stack, post-quantum, fully homomorphic encrypted messaging application using ring-LWE in PHP + SQL + Python.

RESOURCES:

- Original Python: https://blog.openmined.org/build-an-homomorphic-encryption-scheme-from-scratch-with-python/
- ring-LWE notes: https://math.colorado.edu/~kstange/teaching-resources/crypto/RingLWE-notes.pdf
- NIST Post-Quantum: https://csrc.nist.gov/projects/post-quantum-cryptography
- Red Hat Post-Quantum/Lattices: https://www.redhat.com/en/blog/post-quantum-cryptography-lattice-based-cryptography
- Latticed-based cryptography: https://thelatticeclub.com

---

SQL: 

Three tables are required to store login_info, messages, and public_keys.

login_info:
  username CHAR(14)
  password CHAR(60)

Passwords are hashed using standard hashing. 

messages:
  from CHAR(14)
  to CHAR(14)
  message VARCHAR(8000)

Messages are stored encrypted. There is an inflation ratio of ~192.

public_keys:
  username CHAR(14)
  public_key CHAR(192)

Public keys are a single string representing two (reduced cyclotomic) polynomials which are each arrays of ints.

PHP:

Used to handle basic account creation, login, and SQL insertions/lookups. 

Python:

Scripts are executed directly using `escapeshellcmd` and `shell_exec`. Output is printed and passed back as a string.
  
