from flask import Flask
import os
import subprocess

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function
directory = '/home'

@app.route('/')
def bash_script():
    print('omg')
    return 'omg'

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
        subprocess.run(['bash', update_script], check=True)
    except subprocess.CalledProcessError as error:
        print(f"Something terrible happened when running the updater script: {error}")

    return id
    


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
