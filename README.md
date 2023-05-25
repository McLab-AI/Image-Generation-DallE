# Image-Generation WebApp
building an simple Image Generation web app using Dall-E and Streamlit framework

# Setup Dependency
> pip install -r requirements.txt

> streamlit dalle-webapp.py

# dalle-E CLI

curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-openAI-key" \
  -d '{
    "prompt": "a logo of AI and data Error Lab",
    "n":1,
    "size":"1024x1024"
   }'

