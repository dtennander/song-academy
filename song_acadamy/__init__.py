import os

from flask import Flask

root_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(root_dir, 'templates'),
    static_folder=os.path.join(root_dir, 'static'))

import song_acadamy.views
import song_acadamy.api

if __name__ == '__main__':
    app.run(port=8080)
