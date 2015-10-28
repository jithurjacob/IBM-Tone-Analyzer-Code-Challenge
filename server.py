import os, sys, requests, json
from flask import Flask, render_template, request,url_for,jsonify
app = Flask(__name__)
port = os.getenv('VCAP_APP_PORT', '5000')
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/tone/')
def tone():
	
	try:
		#Check if app is in BlueMix Environment
		if 'VCAP_SERVICES' in os.environ:
			vcap_services = json.loads(os.environ['VCAP_SERVICES'])
			svcName="tone"
			if svcName in vcap_services:
				return "Service Found"
			else:
				srvcs=[]
				for srv in vcap_services:
					srvcs.append(srv)
				return "Service is not present"," ".join(srvcs)
		else:
			return ("VCAP is none")
	except Exception, e:
		return ('Error')

	return 'Ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

