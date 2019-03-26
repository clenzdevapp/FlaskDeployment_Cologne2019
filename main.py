from flask import Flask, render_template

app=Flask(__name__)#MODEL

@app.route("/")#CONTROLLER
def index():
    return "Hello SmartNinja!!!"

if __name__ == '__main__':
    app.run()