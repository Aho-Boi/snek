from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route('/')
def index():
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  templateData = {
    'title' : 'test!',
    'time' : timeString
  }
  return render_template('index.html', **templateData)

if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')
