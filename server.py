from flask_app import app

from flask_app.controllers.dojos import Dojo
from flask_app.controllers.ninjas import Ninja

if __name__=='__main__':
    app.run(debug=True)