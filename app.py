from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://root:1234@cluster0.yn8vc.mongodb.net/?retryWrites=true&w=majority')
db = client['kong']
collection = db['fans']


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name = request.form['name']
    comment = request.form['comment']
    print(name,comment);

    post = { "name": name, "comment": comment }
    collection.insert_one(post)

    return jsonify({'msg':'팬명록 등록완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    posts = list(collection.find({},{"_id":False}))
    print(posts)
    return jsonify({"posts":posts})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)