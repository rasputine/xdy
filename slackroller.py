import os
from dice import Roll
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def roller():
	rollString=request.args.get('text') if request.args.has_key('text') else request.args.get('roll',"1d6")
	if rollString[0]=="'" or rollString[0]=='"':
		rollString=rollString[2:-1]
	dice = Roll.from_string(rollString)
	response = {
	"response_type" : "in_channel",
	"text": "Rolled %s and got: *%d*" % (rollString, int(dice)),
	"attachments":[
	    {
	    "text": "%s + %d" % (str(dice), dice.plus) if dice.plus else str(dice.results)
	    }
		]
	}
	return jsonify(response)