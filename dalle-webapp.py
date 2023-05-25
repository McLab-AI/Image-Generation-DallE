"""
@title Dalle streamit Web Appp
@author: mychen76@gmail.com
"""
import openai
import streamlit as st
import urllib.request
from PIL import Image

openai.api_key = "sk-x"  # replace with your key here

def generate_image(image_description):
  img_response = openai.Image.create(
    prompt = image_description,
    n=1,  # specify number of images return
    size="512x512")
  img_url = img_response['data'][0]['url']
  urllib.request.urlretrieve(img_url, 'img.png')
  img = Image.open("img.png")
  return img

# page title
st.title('OpenAI DALL.E - Image Generation')

# text input box 
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    generated_img = generate_image(img_description)
    st.image(generated_img)

    
