
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import os

app = Flask(__name__)
#app = Flask(__name__, template_folder='/var/www/html/templates')

#background process happening without any refreshing
@app.route('/left')
def left():
    print ("Left")
    os.system("python servo.py 1 2 0.1 1")       
    return ("nothing")

@app.route('/center')
def center():
    print ("Center")
    os.system("python servo.py 89 90 0.3 1")       
    return ("nothing")

@app.route('/right')
def right():
    print ("Right")
    os.system("python servo.py 179 180 0.1 1")       
    return ("nothing")


@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
