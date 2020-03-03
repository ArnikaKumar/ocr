from flask import Flask, render_template, request
import json
  
app = Flask(__name__) 
  
@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/getDetails',methods=['POST']) 
# This is not working for now
def getDetails():
    img = request.files['pic']
    lang = request.form['lang']
    payload = {'isOverlayRequired': False, 'apikey': 'b7c4ae2c5b88957', 'url':img, 'language': lang}
    r = request.post('https://api.ocr.space/parse/image', data=payload)
    content = json.loads(r.content.decode())
    text = content['ParsedResults'][0]['ParsedText']
    return text
  
if __name__ == '__main__': 
    #app.run(debug=True) 
    app.run(threaded=True, port=5000)
