from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
import subprocess
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins = "*")
CORS(app)

# directory = '/home/travis/Documents/coding-projects'
directory = '/home'

@app.route('/')
def bash_script():
    print('omg')
    return [
        {'thingone': 'wow'}
    ]

@app.route('/scan-folders')
def list_folders():
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

@app.route('/update-app/<id>')
def update_app(id):
    update_script = 'update-site.sh'

    # Run the updater script
    try:
        subprocess.run(['bash', update_script, id], check=True)
    except subprocess.CalledProcessError as error:
        print(f"Something terrible happened when running the updater script: {error}")
    return id

@app.route('/assupdate', methods=['POST'])
def assupdate():
    #argument, which button was clicked on the frontent. Frontent needs to send json data like {'argument': button_clicked}
    argument = request.get_json()
    print('GOMGOMGOMGOMGOMGOMGOMGOMGOMGOMGOMGOMGOMG', argument['smell'])
    def run_script():
        process = subprocess.Popen(['./update-site.sh', argument['smell']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        for line in iter(process.stdout.readline, b''):
            print('linnne', line)
            socketio.emit('update', {'data': line.decode('utf-8')})
        process.stdout.close()
        process.wait()
        socketio.emit('update', {'data': 'Script finished pooass'})
        return
    thread = threading.Thread(target=run_script)
    thread.start()
    # return jsonify({"status": 200})
    return 
    


# Run the application
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
