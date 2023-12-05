
from flask import Flask, request,render_template,url_for,jsonify
from pymongo import MongoClient
from flask_cors import CORS
from bson import ObjectId
app = Flask(__name__ ,template_folder='templates',static_folder='static')

CORS(app)
#connecting to database 
app.config["MONGO_URI"]="mongodb+srv://ilef:ilef@cluster0.bnfceui.mongodb.net/test"



client = MongoClient(app.config["MONGO_URI"])
db=client.get_database('SAKURAPASTA')
@app.route ('/')
def home ():
    
    return render_template("index.html")
###############################################
##ROUTING###
############
@app.route ('/index.html')
def right():
    return render_template("index.html")

@app.route ('/templates/index.html')
def index():
    return render_template("index.html")

@app.route ('/Reservation.html')
def reser():
    return render_template("Reservation.html")

@app.route ('/templates/Reservation.html')
def vasion():
    return render_template("Reservation.html")

@app.route ('/catalogue.html')
def cat():
    return render_template("catalogue.html")

@app.route ('/templates/catalogue.html')
def talogue():
    return render_template("catalogue.html")

@app.route ('/contact.html')
def act():
    return render_template("contact.html")

@app.route ('/templates/contact.html')
def cont():
    return render_template("contact.html")
@app.route ('/food_menu.html')
def menu():
    return render_template("food_menu.html")

@app.route ('/templates/food_menu.html')
def me():
    return render_template("food_menu.html")

@app.route ('/auth.html')
def au():
    return render_template("auth.html")

@app.route ('/gestion-menu.html')
def gestion():
    return render_template("gestion-menu.html")
############################################
@app.route('/consultres', methods=['POST'])
def deli():
    #data = request.get_json('data')
  
    # print(data)
    # id = request.args.get('data')
    id = request.form 
    print(id)
    num =id['data']
    print(num)
    #print(form_data)
    #db['reservation'].delete_one({'_id': ObjectId(id)})

    allData = db['reservation'].find()
    for data in allData:
        if(num == data['Telephone']):
           db['reservation'].delete_one(data)
           print('deleteddddddd') 
           break

    allData = db['reservation'].find()
    dataJson = []
    for data in allData:
        id = data['_id']
        NometPrenom = data['Nom et Prenom']
        Email = data['Email']           
        NombrePersonne = data['NombrePersonne']
        Telephone = data['Telephone']
        Date = data['Date']
        Temps = data['Temps']
        InfoSupp = data['InfoSupp']
        dataDict = {
                '_id': str(id),
                'Nom et Prenom':NometPrenom,
                'Email':Email,
                'NombrePersonne':NombrePersonne,
                'Telephone' :Telephone,
                'Date' :Date,
                'Temps' :Temps,
                'InfoSupp':InfoSupp
            }
        dataJson.append(dataDict)
    data=dataJson
    print(data)
    return render_template('consultres.html', data=data)

################################################""

@app.route('/reservation', methods=['POST'])
def reservation():
    if (request.method=='POST'):
        print("here")
        
        default_value='pas d information supplementaire'
        NometPrenom =request.form.get('NometPrenom')
        print(NometPrenom)
        Email =request.form.get('Email')
        NombrePersonne =request.form.get('NombrePersonne')
        Telephone  =request.form.get('Telephone')
        Date =request.form.get('Date')
        Temps =request.form.get('Temps')
        InfoSupp =request.form.get('InfoSupp',default_value)
        db['reservation'].insert_one({
                'Nom et Prenom':NometPrenom,
                    'Email':Email,
                    'NombrePersonne':NombrePersonne,
                    'Telephone':Telephone,
                    'Date' :Date,
                    'Temps' :Temps,
                    'InfoSupp':InfoSupp
                })
        
        return render_template("index.html")

############################################""
        
#data from atlas mongo db to ihm
@app.route('/consultres.html', methods=['GET'])

def get_all_data():
    allData = db['reservation'].find()
    dataJson = []
    for data in allData:
        id = data['_id']
        NometPrenom = data['Nom et Prenom']
        Email = data['Email']           
        NombrePersonne = data['NombrePersonne']
        Telephone = data['Telephone']
        Date = data['Date']
        Temps = data['Temps']
        InfoSupp = data['InfoSupp']
        dataDict = {
                '_id': str(id),
                'Nom et Prenom':NometPrenom,
                'Email':Email,
                'NombrePersonne':NombrePersonne,
                'Telephone' :Telephone,
                'Date' :Date,
                'Temps' :Temps,
                'InfoSupp':InfoSupp
            }
        dataJson.append(dataDict)
    data=dataJson
    print(data)
    return render_template('consultres.html', data=data)

    ##################################################



if __name__ == "__main__":
    app.run(debug=True)