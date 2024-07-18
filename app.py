from flask import Flask
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
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
    


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
