import streamlit as st
import math as m
from Crypto.Util.number import isPrime

st.title("RSA Encryption and Decryption")
st.write("This is a simple implementation of RSA encryption and decryption algorithm.")
st.write("By: Abdulrahman Tabaza and Omar Quishawi")

# Ask the user for p, q, and e
col1, col2, col3 = st.columns(3)

with col1:
    p = st.number_input("Enter a prime number (p): ", value=17)
    if not isPrime(p):
        st.error("p must be a prime number")
with col2:
    q = st.number_input("Enter a different prime number (q): ", value=11)
    if not isPrime(q):
        st.error("q must be a prime number")
    if p == q:
        st.error("p and q must be different")
with col3:
    e = st.number_input("Enter an integer (e): ", value=3)
    st.write("e is usually set to 3, 5, 17 or 65537.")


public_key = None
private_key = None

if (p != q) and (isPrime(p) and isPrime(q)):
    try:
        # Generate the keys for RSA
        n = p * q
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)  # Calculate the modular multiplicative inverse of e mod phi
        public_key = (e, n)
        private_key = (d, n)

    except Exception as e:
        st.error("Error: " + str(e))

if public_key and private_key:
    st.success("Keys Generated Successfully")
    with st.expander("Show Keys"):
        st.write(f"Public Key: {public_key}")
        st.write(f"Private Key: {private_key}")

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

if public_key:
    with tab1:

        text = st.text_input("Enter a small text to encrypt: ")
        if text:
            encrypted_text = ' '.join(str(pow(ord(char), e, n)) for char in text)
            st.write(f"Encrypted Text: {encrypted_text}")

if private_key:
    with tab2:

        text = st.text_input("Enter a list of numbers to decrypt (separated by space): ")
        if text:
            text = list(map(int, text.split()))
            decrypted_text = ''.join(chr(pow(char, d, n)) for char in text)
            st.write(f"Decrypted Text: {decrypted_text}")