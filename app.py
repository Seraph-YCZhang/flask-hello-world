from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

print(os.environ.get('OPENAI_API_KEY'))
client = OpenAI(
)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        # ""Generate an ambience  image inspired by Floyd wright style. Capture the essence of a rich and festive interior with no people present. The scene should have Chrismas elements and holiday colorful light strips.Create the image in a two-point perspective from the left side of the room. For casual live style.""
        response = client.images.generate(
        model="dall-e-3",
        # prompt="generate one ambience image like style of Frank Lloyd Wright's interior work, cozy, warm, no people, indoor, Two-point perspective, interior design rendering visual style, no outlines",
        size="1792x1024",
        # prompt="Generate an ambience image inspired by Liang Sicheng and  Siheyuan style. Capture the essence of a rich and festive interior with no people present. The setting should have Dou Gong Brackets, Decorative Beams, Spring Festival Couplets, Fu Character and Wooden Structure.Create the image in a two-point perspective from the left side of the interior. For casual live style. With spring festival theme added",
        prompt=prompt,

        quality="standard",
        # style="natural", "vivid"
        n=1,
        )
        print('image', response.data)
        image_url = response.data[0].url
        revised_prompt= response.data[0].revised_prompt
       
        return redirect(url_for("index", url=image_url, revised_prompt=revised_prompt,prompt=prompt))

    image_url = request.args.get("url")
    revised_prompt = request.args.get("revised_prompt")
    prompt = request.args.get("prompt")
    return render_template("index.html",url=image_url, revised_prompt=revised_prompt,prompt=prompt)

@app.route('/hello')
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
    # prompt="generate one ambience image like style of Frank Lloyd Wright's interior work, cozy, warm, no people, indoor, Two-point perspective, interior design rendering visual style, no outlines",
    size="1792x1024",
    # prompt="Generate an ambience image inspired by Liang Sicheng and  Siheyuan style. Capture the essence of a rich and festive interior with no people present. The setting should have Dou Gong Brackets, Decorative Beams, Spring Festival Couplets, Fu Character and Wooden Structure.Create the image in a two-point perspective from the left side of the interior. For casual live style. With spring festival theme added",
        prompt="Generate an ambience  image inspired by Floyd wright style. Capture the essence of a rich and festive interior with no people present. The scene should have Chrismas elements and holiday colorful light strips.Create the image in a two-point perspective from the left side of the room. For casual live style.",

    quality="standard",
    # style="natural", "vivid"
    n=1,
    )
    print('image', response.data)
    image_url = response.data[0].url
    return image_url


