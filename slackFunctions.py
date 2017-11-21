from slackclient import SlackClient

genChannelID = 'C80BTQK89'
botAccessToken = "xoxb-274946054277-Xz1N5kZfIiHOUk4QBKxORXL0"
botName = "helloat12"

attachments_json = [
    {
    	"fallback": "whats up",
        "color": "#ABCDE1",
        "attachment_type": "default",
        "callback_id": "buttons",

        "actions": [ {
        	"name": "timezone",
            "text": "Pick a timezone",
        	"type": "select"
        	}
        ]
    }
]

slackClient = SlackClient(botAccessToken)

def sendMessage(channelID='C80BTQK89', msg="Hi"):
# send a message to a given channel, as the bot
    slackClient.api_call("chat.postMessage", channel=channelID, text = msg)

def interactMenu(options):
# sending a drop down menu with a list of timezones

	zoneOption = dict()
	optionsList = list()

	for zone in options:
		zoneOption["text"] = zone
		zoneOption["value"] = zone
		optionsList.append(zoneOption)
		zoneOption = dict()

	attachments_json[0]["actions"][0]["options"] = optionsList

	slackClient.api_call("chat.postMessage", channel=genChannelID, text="That was not too clear... could you pick from these?", attachments=attachments_json)
