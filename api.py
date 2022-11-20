from flask import Flask,jsonify,request
app=Flask(__name__)

Task=[
    {
        "id":1,
        "title":u"buy groceries",
        "description":u"Fruits, Cereal, Bread",
        "done":False
    },
    {
        "id":2,
        "title":u"Do Work",
        "description":u"study-Math-English-Science,cupboardOrganisation",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please Provide Data In Correct Format"
        },400)
    t={
       
        "id":Task[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    Task.append(t)
    return jsonify({
                "status":"Success",
                "message":"Task Added Successfully"
            })

@app.route("/get-data")
def getTask():
    return jsonify({
        "data":Task
    })

@app.route("/")
def HelloWorld():
    return "Hello World"


if(__name__=="__main__"):
    app.run(debug=True)