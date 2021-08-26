from flask import Flask
import time
from flask import jsonify


app = Flask(__name__)

@app.route('/weight_machine/weigh', methods=['GET'])
def welcome():
    try:
        time.sleep(10)
        thisdict = {
            "status": "success",
            "response": {
                "weight": 11
            },
        }
        return jsonify(thisdict) 
    except:
        thisdict = {
            "status": "error",
            "response": {

            },
        }
        return jsonify(thisdict) 


if __name__ == '__main__':
    app.run(debug=True)