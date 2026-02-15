from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    images = [
        "foto1_16x9.jpg",
        "foto2_16x9.jpg",
        "foto3_16x9.jpg",
        "foto4_16x9.jpg",
        "foto5_16x9.jpg"
    ]
    selected_image = random.choice(images)
    return render_template("index.html", hero_image=selected_image)

if __name__ == "__main__":
    app.run(debug=True)
