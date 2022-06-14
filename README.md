client = MongoClient('mongodb+srv://root:1234@cluster0.yn8vc.mongodb.net/?retryWrites=true&w=majority')
db = client['kong']
collection = db['fans']
