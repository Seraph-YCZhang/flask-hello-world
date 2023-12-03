from flask import Flask
from openai import OpenAI

app = Flask(__name__)

OPEN_AI_KEY  = "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"

client = OpenAI(
    api_key=OPEN_AI_KEY
)

@app.route('/')
def hello_world():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )
    msg =  completion.choices[0].message.content
    print('msg', completion)
    return msg



@app.route('/image')
def gen_image():
    response = client.images.generate(
    model="dall-e-3",
    prompt="ambience image, cozy, warm, no people, outdoor",
    size="1792x1024",
    quality="standard",
    n=1,
    )
    print('image', response.data)
    image_url = response.data[0].url
    return image_url


