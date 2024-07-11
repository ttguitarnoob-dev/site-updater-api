from flask import Flask
import os

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function
directory = '/home'

@app.route('/')
def bash_script():
    print('omg')

@app.route('/scan-folders')
def list_folders():
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
