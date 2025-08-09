from flask import Flask, render_template, Response
from utils import generate_frames  # Import the frame generator function

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML template for displaying the video stream
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
