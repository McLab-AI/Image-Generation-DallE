curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-openai-key-here" \
  -d '{
    "prompt": "a logo of AI and data Error Lab",
    "n":1,
    "size":"1024x1024"
   }'
