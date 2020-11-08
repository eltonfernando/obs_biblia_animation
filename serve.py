from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route("/texto")
def index():
  return render_template('index.html')

if __name__ == "__main__":
 obj=app.run()