from E_voting import db
from E_voting import app







if __name__ == "__main__":
    db.create_all()
    # db.drop_all()
    app.run(debug=False) 
    # app.run(host='0.0.0.0', debug=True, port=5000)




