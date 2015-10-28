import os, sys, requests, json
from flask import Flask, render_template, request,url_for,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/tone')
def tone():
	try:
		#Check if app is in BlueMix Environment
        if 'VCAP_SERVICES' in os.environ:
            
            #3. Read Connection Parameters from VCAP_SERVICES Environment Variable

            #convert vcap-services json into a dictionary
            vcap_services = json.loads(os.environ['VCAP_SERVICES'])
            srvcs=[]
            for svc in vcap_services:
            	srvcs.append(svc)
			return jsonify(srvcs)
		else:
			return jsonify("VCAP is none")
	except Exception, e:
		return jsonify('Error')

    return 'Hello World'

if __name__ == "__main__":
    app.run()

