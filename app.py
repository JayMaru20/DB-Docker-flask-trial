from config import app
import routes

@app.route("/")
def hello():
    return "Hello!!! running"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")