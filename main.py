from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                .error {{
                    color: red;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                <label>Rotate by:
                    <input name="rot" type="text" value="{rot}">
                </label>
                <textarea name="text">{text}</textarea>
                <input type="submit" value="Submit Query">
            </form>
            <p class="error">{val_error}</p>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form.format(val_error="",text="",rot="0")

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]

    if not rot or not is_integer(rot):
        return form.format(val_error="Rotate value must be an integer",
        text=text,
        rot=rot)
    
    encrypted_text = rotate_string(text,int(rot))

    return form.format(val_error="",
    text=encrypted_text,
    rot=rot)

app.run()