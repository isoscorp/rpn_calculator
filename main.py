from api import api, app
from endpoint import namespace

api.add_namespace(namespace)


if __name__ == '__main__':
    app.run(debug=True)
