from flask import Flask
import zeep
import serviceSoap
from flask import jsonify
  
app = Flask(__name__)

@app . route( '/')
def home():
    return  'home'  

    
@app . route( '/infos/<code>' )
def getInfos(code):
    # t =[{}]
    # t= test.Infos_pays(code)
    #return ("bonjour")
    return  jsonify(serviceSoap.Infos_pays(code))

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"

    return response
 
 
if __name__ == '__main__':
    app.run(debug=True)
    