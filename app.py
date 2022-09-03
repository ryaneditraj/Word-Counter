from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        txt_len = len(text)
        print(txt_len)
        tl = txt_len
        wc = 1
        if text == '':
            wc = 0
        else:
            for i in text:
                
                if i == " ":
                    wc+=1
        print(wc)
        return render_template('index.html', wc = wc, tl = tl, text = text)
    return render_template('index.html')

app.run(debug=True)