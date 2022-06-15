from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://root:1234@cluster0.yn8vc.mongodb.net/?retryWrites=true&w=majority')
db = client['kong']
collection = db['bucket']


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    buckets = list(collection.find({},{'_id':False}))

    doc = {
        'num':len(buckets)+1,
        'bucket':bucket_receive,
        'done':0
    }

    collection.insert_one(doc)

    print(bucket_receive)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num = int(request.form['num'])
    print(num)
    collection.update_one({'num':num},{'$set':{'done':1}})

    return jsonify({'msg': '완료!'})

@app.route("/bucket/cancel", methods=["POST"])
def bucket_cancel():
    num = int(request.form['num'])
    print(num)
    collection.update_one({'num':num},{'$set':{'done':0}})

    return jsonify({'msg': '완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():

    buckets = list(collection.find({},{'_id':False}))

    return jsonify({'buckets': buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)