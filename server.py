import os, sys, requests, json
from flask import Flask, render_template, request,url_for,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/tone/')
def tone():
	
	try:
		#Check if app is in BlueMix Environment
		if 'VCAP_SERVICES' in os.environ:
			vcap_services = json.loads(os.environ['VCAP_SERVICES'])
			for svc in vcap_services:
				srvcs.append(svc)
			return (srvcs)
		else:
			return ("VCAP is none")
	except Exception, e:
		return jsonify('Error')

	return 'Hello World'

if __name__ == "__main__":
    app.run()

