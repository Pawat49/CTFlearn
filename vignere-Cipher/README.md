# Vigenère Cipher

## Description

The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.

I’m not sure what this means, but it was left lying around: `blorpy`

Ciphertext: `gwox{RgqssihYspOntqpxs}`

## Solution

We are given the ciphertext and what appears to be the key (`blorpy`). We can use a decoding tool to reverse the Vigenère cipher.

1. Navigate to [CyberChef](https://gchq.github.io/CyberChef/).
2. Select the "Vigenère Decode" recipe.
3. Input the ciphertext: `gwox{RgqssihYspOntqpxs}`.
4. Input the key: `blorpy`.
5. The decoded output will reveal the flag.

![CyberChef Decoding Screenshot](/vignere-Cipher/Screenshot%202026-05-27%20141626.png)

## Flag

`flag{CiphersAreAwesome}`