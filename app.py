# app.py
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['userInput']
    if 'fileInput' in request.files:
        uploaded_file = request.files['fileInput']
        if uploaded_file.filename != '':
            uploaded_file.save('static/uploaded_image.jpg')
            image_url = url_for('static', filename='uploaded_image.jpg')
            result = "Das Ergebnis der Addition von 5 und " + user_input + " ist " + str(5 + int(user_input))
            return f'Deine Ergebnis: {result}<br><img src="{image_url}" alt="Uploaded Image">'
    
    # Wenn kein Bild hochgeladen wurde
    result = "Das Ergebnis der Addition von 5 und " + user_input + " ist " + str(5 + int(user_input))
    return f'Dein Ergebnis: {result}'

if __name__ == '__main__':
    app.run(debug=True)
