from flask import Flask
from flask import render_template
from flask import Response
from camera import VideoCamera

app = Flask(__name__)
@app.route('/') # / k pehle IP jayga ,, rasp pi ka ip address k aage / lga k commands likhenge
def index():
	return render_template('index.html')

def gen(camera):
	while True: #live feed
		frame = camera.get_frame()  # camera k feed se frame
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_bw(camera):
	while True:
		frame = camera.get_frame_bw()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_hr(camera):
	while True:
		frame = camera.get_frame_hr()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_rm(camera):
	while True:
		frame = camera.get_frame_rm()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_gm(camera):
	while True:
		frame = camera.get_frame_gm()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_bm(camera):
	while True:
		frame = camera.get_frame_bm()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def image(camera):
	frame = camera.get_frame()
	return frame

@app.route('/video_feed')
def video_feed():
	return Response(gen(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/bw')
def video_feed_bw():
	return Response(gen_bw(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/hr')
def video_feed_hr():
	return Response(gen_hr(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/rm')
def video_feed_rm():
	return Response(gen_rm(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/bm')
def video_feed_bm():
	return Response(gen_bm(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/gm')
def video_feed_gm():
	return Response(gen_gm(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/shot.jpg')
def shot_feed():
	return Response(image(VideoCamera()),
					mimetype='image/jpeg')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	# , debug=True
