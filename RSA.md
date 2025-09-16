# RSA Cryptosystem

**Public key cryptosystem**: Relies heavily on the integer factorization (trapdoor function): validating the result by multiplying two numbers is quite easy but finding the factors is hard.

## Step 1: 

Generate **2** large prime number **p** and **q**

## Step 2:

Calculate **n = p * q**, and **phi(n) = (p-1) * (q-1)**

## Step 3:

Calculate **e** (public key) such that **e** and **phi(n)** are relative primes.

## Step 4:

Calculate **d** (private key): modular inverse of **e**.

**(d * e) % phi(n) = 1**

So we have: 

PUBLIC KEY: (e , n) 

PRIVATE KEY (d , n)



