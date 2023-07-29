from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
  return '<h1 style="color: blue">Welcome to ITIL exam...! </h1>'

@app.route("/modules", methods=["GET"])
def module():
	return '<h3 style="color:orange">DITISS Course module names :- 1.FCN 2.COSA 3.Security Concepts 4.DevOps 5.NDC 6.PKI 7.Cyber Forensics 8.Compliance Audit</h1>'

@app.route("/me", methods=["GET"]) 
def me():
  return '<h1 style="color:purple">230344223055, Yatin Suresh Chaudhari, 8104694273</h1>'

app.run(port=4000, host="0.0.0.0", debug=True)  

