from flask import Flask, request, send_from_directory, redirect, send_file, render_template
import os,cv2
import neuralStyleProcess

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("upload.html")
@app.route("/upload", methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print("TARGET", target)
	if not os.path.isdir(target):
		os.mkdir(target)
	else:
		print("Couldn't create upload directory: {}".format(target))
	data = request.form.get("style")
	print(data)
	myFiles = []
	for file in request.files.getlist("file"):
		print("file", file)
		filename = file.filename
		print("filename", filename)
		destination = "".join([target, filename])
		print("destination", destination)
		file.save(destination)
		myFiles.append(filename)
	print(myFiles)

	return render_template("complete.html", image_names=myFiles, selected_style=data)

# This function takes the parameter name <filename>
@app.route('/upload/<filename>')
def send_original_image(filename):
	return send_from_directory("images", filename)

@app.route('/complete/<filename>/<selected_style>')
def send_processed_image(filename, selected_style):
	directoryName = os.path.join(APP_ROOT, 'images/')
	newImg = neuralStyleProcess.neuralStyleTransfer(directoryName, filename, selected_style)
	return send_from_directory("images", newImg)

if __name__ == '__main__':
    app.run()
