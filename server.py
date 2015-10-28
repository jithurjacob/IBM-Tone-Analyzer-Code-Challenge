import os, sys, requests, json
from flask import Flask, render_template, request,url_for,jsonify,make_response
app = Flask(__name__)
port = os.getenv('VCAP_APP_PORT', '5000')
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/tone/', methods = ['POST'])
def tone():
	
	try:
		#Check if app is in BlueMix Environment
		if 'VCAP_SERVICES' in os.environ:
			vcap_services = json.loads(os.environ['VCAP_SERVICES'])
			svcName="tone_analyzer"
			if svcName in vcap_services:
				svc = vcap_services[svcName][0]['credentials']
				url = svc['url']+"/v1/tone"
				user = svc['username']
				password = svc['password']
				data={'text': (request.form['text'])}
				r = requests.post(url,auth=(user,password),headers = {'content-type': 'application/json'},data=json.dumps(data))
				if r.status_code!=200:
					try:
						error = json.loads(r.text)
					except:
						raise Exception("API error, http status code %d" % r.status_code)
						raise Exception("API error %s: %s" % (error['error_code'], error['user_message']))

				return json.loads(r.text)
			else:
				srvcs=[]
				for srv in vcap_services:
					srvcs.append(srv)
				message = {'message': "Service is not present"+" ".join(srvcs)}
				return make_response(json.dumps(message),200)
				
		else:
			return ("VCAP is none")
	except Exception, e:
		return ('Error',e)

	return 'Ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

