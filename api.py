from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def translate():
    english_text = request.args.get('english_text')
    if english_text:
        # perform translation
        return arabic_translation
    else:
        return 'Please provide an English text to translate.'

if __name__ == '__main__':
    app.run(debug=True)
