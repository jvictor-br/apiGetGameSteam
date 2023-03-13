# SERVER
from flask import Flask, request, render_template
from flask_cors import CORS
import requests
import json

appid = ''
app = Flask(__name__)
headers = {"Accept-Language":"pt-BR,pt;"}
CORS(app)
@app.route("/api", methods=["GET"])
def api():
    print("iniciou request")
    try:
        appid = request.headers["appid"]
        jogoinfo = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}&l=portugues",headers=headers)
        dados = jogoinfo.json()[appid]['data']
        interesse = ["name","header_image","background","developers","publishers","metacritic","release_date","categories"]
        res = {}
        categories = []
        for i in interesse:
            try:
                res[i] = dados[i]
            except:
                res[i] = []
        for i in res["categories"]:
            categories.append(i["description"])
        print(categories)
        res.pop("categories")
        res["categories"] = categories
        res = json.dumps(res)
        print("resposta final")
        
        response = app.response_class(
                response=res,
                status=200,
                mimetype='application/json'
            )
        return response
    except Exception:
        try:
            response = app.response_class(
                    response= jogoinfo,
                    status=200,
                )
            return response
        except Exception:
            response = app.response_class(
                    response= "Algo deu errado",
                    status=404,
                )
            return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html")

app.run(threaded=True, host='0.0.0.0',port=5000)