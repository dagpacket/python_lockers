from flask import  Flask, redirect, url_for, request, jsonify
import time
import serial
import json
class EmptySerialResponseException(Exception):
    pass
SERIAL_PORT_NAME = '/dev/ttyS1'

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
@app.route('/locker/open', methods=['POST'])
def open_locker():
    try:
        request_data = request.get_json()

        ser = serial.Serial(SERIAL_PORT_NAME)

        request = {
        "Box": [request_data["id"], request_data["number"]],
        "command": 'open',
        }

        requestJson = json.dumps(request)
        ser.write(bytes(requestJson), encoding='ascii')
        response = ''

        with serial.Serial(SERIAL_PORT_NAME, 19200, timeout=1) as ser:
            response = ser.readline()
        if bool(response) == False:
            raise EmptySerialResponseException('Se obtuvo una respuesta vacia')
        serialResponseJson = json.loads(response)
        if hasattr(serialResponseJson, 'status'):
            print(json.dumps(response)) 

    except EmptySerialResponseException as err:
        pass
        print( json.dumps({'error' : 'respuesta vacia'}))

    except Exception as e:
        pass
        print( json.dumps({'error' : e}));


@app.route('/locker/scan', methods=['POST'])
def scan_locker():
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)
        request_data = request.get_json()
        request = {
        "Box": [request_data["id"], request_data["number"]],
        "command": 'scan',
        }
        requestJson = json.dumps(request)
        ser.write(bytes(requestJson), encoding='ascii')
        response = ''
        with serial.Serial(SERIAL_PORT_NAME, 19200, timeout=1) as ser:
            response = ser.readline()
        if bool(response) == False:
            raise EmptySerialResponseException('Se obtuvo una respuesta vacia')
        
        serialResponseJson = json.loads(response)
        
        if  hasattr(serialResponseJson, 'active') or hasattr(serialResponseJson, 'isLoaded') or hasattr(serialResponseJson, 'isOpen') :        
            print(json.dumps(response)) 

    except EmptySerialResponseException as err:
        pass
        print(json.dumps({'error' : 'respuesta vacia'})) 

    except Exception as e:
        pass
        print(json.dumps({'error' : 'error general'}))


@app.route('/weighing_machine/get', methods=['GET'])
def weighing_machine():
        try:
            ser = serial.Serial(SERIAL_PORT_NAME)
            request = {
                "command": 'getWeight',
            }
            requestJson = json.dumps(request)
            ser.write(bytes(requestJson), encoding='ascii')
            response = ''
            with serial.Serial(SERIAL_PORT_NAME, 19200, timeout=1) as ser:
                response = ser.readline()
            if bool(response) == False:
                raise EmptySerialResponseException('Se obtuvo una respuesta vacia')

            serialResponseJson = json.loads(response)

            if  hasattr(serialResponseJson, 'weight'):        
                print (json.dumps(response))

        except EmptySerialResponseException as err:
            pass
            print (json.dumps({'error' : 'respuesta vacia'}))

        except Exception as e:
            pass
            print (json.dumps({'error' : 'error general'}))


#execute_command("openLoaded")
#execute_command("getWeight")

#execute_command("openScale")

#execute_command("serviceOn")

#execute_command("serviceOff")
#execute_command("operating")

#execute_command("idle")
@app.route('/general_commands', methods=['POST'])
def execute_command(command):
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)
        request_data = request.get_json()
        request = {
            "command": request_data["command"],
        }
        requestJson = json.dumps(request)
        ser.write(bytes(requestJson), encoding='ascii')
        response = ''
        with serial.Serial(SERIAL_PORT_NAME, 19200, timeout=1) as ser:
            response = ser.readline()
        if bool(response) == False:
            raise EmptySerialResponseException('Se obtuvo una respuesta vacia')
        
        serialResponseJson = json.loads(response)
        
        if  hasattr(serialResponseJson, 'status'):        
            print(json.dumps(response)) 

    except EmptySerialResponseException as err:
        print(json.dumps({'error' : 'respuesta vacia'})) 

    except Exception as e:
        print(json.dumps({'error' : e})) 
@app.route('/shutdown_alarm', methods=['GET'])
def shutdown_alarm(alarm_state):
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)
        request = {
            "Alarm": alarm_state,
        }
        requestJson = json.dumps(request)
        ser.write(bytes(requestJson), encoding='ascii')
        response = ''
        with serial.Serial(SERIAL_PORT_NAME, 19200, timeout=1) as ser:
            response = ser.readline()
        if bool(response) == False:
            raise EmptySerialResponseException('Se obtuvo una respuesta vacia')
        
        serialResponseJson = json.loads(response)
        
        if  hasattr(serialResponseJson, 'status'):        
            print(json.dumps(response)) 

    except EmptySerialResponseException as err:
        pass
        print(json.dumps({'error' : 'respuesta vacia'})) 

    except Exception as e:
        pass
        print(json.dumps({'error' : 'error general'})) 


if __name__ == '__main__':
    app.run(debug=True)