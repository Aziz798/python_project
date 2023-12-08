from flask_app import app
from flask_app.controllers import houses_in_sell



if __name__=="__main__":
    app.run(debug=True,port=5001)