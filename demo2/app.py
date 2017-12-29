
import time
import  json
from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.


async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)


thread = None
thread_lock = Lock()


@app.route('/')
def index_page():
    return render_template('index.html')

@socketio.on('on_connect', namespace='/socket')
def socket_connect():
   print("connecting.....")
   while True:
       msg1= [{"eid": 49, "rul": 167, "cycle": 67}]
       socketio.emit('message_response_predict', json.dumps(dict(status=200, result=msg1)), namespace='/socket')
       msg2=[{'edata': [{'sdata': [{'data': 518.67, 'cycle': 66}], 'sid': 's1'},
                        {'sdata': [{'data': 642.48, 'cycle': 66}], 'sid': 's2'},
                        {'sdata': [{'data': 1581.22, 'cycle': 40}, {'data': 1579.31, 'cycle': 41}, {'data': 1587.37, 'cycle': 42}, {'data': 1582.75, 'cycle': 43}, {'data': 1583.52, 'cycle': 66}], 'sid': 's3'},
                        {'sdata': [{'data': 1393.19, 'cycle': 66}], 'sid': 's4'},
                        {'sdata': [{'data': 14.62, 'cycle': 66}], 'sid': 's5'}, {'sdata': [{'data': 21.61, 'cycle': 66}], 'sid': 's6'},
                        {'sdata': [{'data': 554.91, 'cycle': 66}], 'sid': 's7'},
                        {'sdata': [{'data': 2388.04, 'cycle': 40}, {'data': 2388.03, 'cycle': 41}, {'data': 2388.03, 'cycle': 42}, {'data': 2387.98, 'cycle': 43}, {'data': 2388.0, 'cycle': 66}], 'sid': 's8'},
                        {'sdata': [{'data': 9061.5, 'cycle': 40}, {'data': 9063.2, 'cycle': 41}, {'data': 9065.04, 'cycle': 42}, {'data': 9060.52, 'cycle': 43}, {'data': 9065.53, 'cycle': 66}], 'sid': 's9'},
                        {'sdata': [{'data': 1.3, 'cycle': 66}], 'sid': 's10'},
                        {'sdata': [{'data': 47.35, 'cycle': 66}], 'sid': 's11'},
                        {'sdata': [{'data': 522.36, 'cycle': 40}, {'data': 522.43, 'cycle': 41}, {'data': 522.01, 'cycle': 42}, {'data': 522.15, 'cycle': 43}, {'data': 522.04, 'cycle': 66}], 'sid': 's12'},
                        {'sdata': [{'data': 2388.02, 'cycle': 66}], 'sid': 's13'},
                        {'sdata': [{'data': 8147.92, 'cycle': 40}, {'data': 8142.86, 'cycle': 41}, {'data': 8141.99, 'cycle': 42}, {'data': 8145.76, 'cycle': 43}, {'data': 8141.03, 'cycle': 66}], 'sid': 's14'},
                        {'sdata': [{'data': 8.385, 'cycle': 66}], 'sid': 's15'},
                        {'sdata': [{'data': 0.03, 'cycle': 66}], 'sid': 's16'},
                        {'sdata': [{'data': 391, 'cycle': 66}], 'sid': 's17'},
                        {'sdata': [{'data': 2388, 'cycle': 66}], 'sid': 's18'},
                        {'sdata': [{'data': 100.0, 'cycle': 66}], 'sid': 's19'},
                        {'sdata': [{'data': 39.12, 'cycle': 40}, {'data': 39.12, 'cycle': 41}, {'data': 39.07, 'cycle': 42}, {'data': 38.94, 'cycle': 43}, {'data': 38.99, 'cycle': 66}], 'sid': 's20'},
                        {'sdata': [{'data': 23.429, 'cycle': 66}], 'sid': 's21'}], 'eid': 49}]
       socketio.emit('message_response_sensor', json.dumps(dict(status=200, result=msg2)), namespace='/socket')
@socketio.on('on_message_predict', namespace='/socket')
def message_predict():
   print("predicting.....")
   msg1 = [{"eid": 49, "rul": 167, "cycle": 67}]
   socketio.emit('message_response_predict', json.dumps(dict(status=200, result=msg1)), namespace='/socket')

@socketio.on('on_message_sensor', namespace='/socket')
def message_sensor(message):
    print("send message....")

@socketio.on('on_disconnect', namespace='/socket')
def socket_disconnect():
    print()

if __name__ == '__main__':
    socketio.run(app, debug=True)