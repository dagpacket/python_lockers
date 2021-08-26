import serial
import json

class EmptySerialResponseException(Exception):
    pass


SERIAL_PORT_NAME = '/dev/ttyS1'
def open_locker(locker):
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)

        request = {
        "Box": [locker.id, locker.number],
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

def scan_locker(locker):
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)
        request = {
        "Box": [locker.id, locker.number],
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

def get_weight():
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

def execute_command(command):
    try:
        ser = serial.Serial(SERIAL_PORT_NAME)
        request = {
            "command": command,
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



def buy_processes():
    try:
        open_weight_machine_door = execute_command("openScale")
        if hasattr(open_weight_machine_door, 'status') and open_weight_machine_door.status == 'fail':
            raise Exception("El locker ya esta ocupado")

        get_weight = execute_command("getWeight")
        if not hasattr(get_weight, 'weight'):
            raise Exception("Error al pesar tu paquete")

        locker_scan = scan_locker({'id': 'D', 'number':5})
        if hasattr(locker_scan, 'isLoaded') and locker_scan.isLoaded == 'true':
            raise Exception("El locker ya esta ocupado")
        
        locker_open = open_locker({'id': 'D', 'number':5})
        if hasattr(locker_open, 'status') and locker_open.status == 'false':
            raise Exception("Hubo un error al abrir el locker")

        ### wait 1 minute
        retries_limit = 12
        retries = 1
        is_locker_door_locked = False
        while not is_locker_door_locked and retries <= retries_limit:
            if (open_locker({'id': 'D', 'number':5}).status == 'true'):
                retries = retries + 1;
                sleep(5)
            is_locker_door_locked = True

            
    except Exception as e:
        pass
        print(json.dumps({'error' : e })) 




### TESTS

# buy_processes()

open_locker({'id': 'D', 'number':3})
scan_locker({'id': 'C', 'number':5})
execute_command("openLoaded")
execute_command("getWeight")

execute_command("openScale")

execute_command("serviceOn")

execute_command("serviceOff")
execute_command("operating")

execute_command("idle")

shutdown_alarm('off')