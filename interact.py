from flask import Flask, request, Response, make_response
from flask_apscheduler import APScheduler
from functions import getOffset, getClosest100
from slackFunctions import interactMenu, sendMessage
import json

class Config(object):
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

slackWebhook = 'GbXzQEIfRgvSHLFH0B1TIB1r'

def setScheduler(zone, timeToSet):
# setting scheduler for a zone
	scheduler.add_job(id = zone, func = 'slackFunctions:sendMessage',  trigger='cron', hour=timeToSet.hour, minute=timeToSet.minute, replace_existing=True)
	print "Scheduled."

@app.route('/slack', methods=['POST'])
def inbound():
	if request.form.get('token') == slackWebhook:
		userName = request.form.get('user_name')
		zone = request.form.get('text')
		
		print userName
		if not userName=="slackbot":
			offset = getOffset(zone)

			if offset:
				setScheduler(zone, offset)
			else:
				options = sorted(getClosest100(zone))
				interactMenu(options)

	return Response(), 200

@app.route("/slack/schedule", methods=["POST"])
def schedule():
    form_json = json.loads(request.form["payload"])

    selection = form_json["actions"][0]["selected_options"][0]["value"]

    setScheduler(selection, getOffset(selection))
    
    return Response(), 200    

if __name__=="__main__":
	sendMessage(msg="What is your timezone?")
	app.run(debug=True)


