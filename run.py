from apps import create_app

# from flaskwebgui import FlaskUI

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5020, host="0.0.0.0")
    # FlaskUI(app=app, server="flask").run()
