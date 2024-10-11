import random
import string
import streamlit as st

st.title('Password Generator')

if st.checkbox('Do you want to have numbers?'):
    has_number = True
else:
    has_number = False

if st.checkbox('Do you want to have special characters?'):
    has_special = True
else:
    has_special = False

def generate_password(min_length, has_number, has_special):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if has_number:
        characters += digits
    if has_special:
        characters += special
    
    pwd = ""

    # at least one number if so chosen
    if has_number:
        new_number = random.choice(digits)
        pwd += new_number

    # at least one special character if so chosen
    if has_special:
        new_special = random.choice(special)
        pwd += new_special


    while len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

    return pwd


min_length = st.slider('Minimal Length', 12, 60, 20)  # min, max, default

pwd = generate_password(min_length, has_number, has_special)

st.subheader('Password')
st.write(pwd)

footer_html = """<div style='text-align: center;'>
  <p><a href="https://github.com/italojsoliveira/password-generator">Source Code</a></p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)

footer_html = """<div style='text-align: right;'>
  <p>Developed with ❤️ by <a href="https://italojsoliveira.github.io/">Ítalo Oliveira</a></p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)

