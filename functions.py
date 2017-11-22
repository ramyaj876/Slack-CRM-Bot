from nltk import edit_distance
from pytz import all_timezones, timezone
from datetime import datetime


timeSet = "12:00"
wordCompare = ""

def compareDistance(word1, word2):
# Comparison for sorting
	global wordCompare
	return edit_distance(wordCompare, word1)-edit_distance(wordCompare, word2)

def getClosest100(zone):
# Top 100 timezones closest to what was entered
	global wordCompare
	wordCompare = zone
	return sorted(all_timezones, cmp=compareDistance)[0:99]

def getOffset(zone):
# Getting the offset for a timezone
	
	# Validity of a given timezone
	valid = None
	for validZone in all_timezones:
		if validZone.lower() == zone.lower():
			valid = True
			zone = validZone
			break
	if not valid:
		return None

	# Getting the India offset
	zoneOffset = datetime.now(timezone(zone)).utcoffset()
	offsetIn = datetime.now(timezone('Asia/Calcutta')).utcoffset()
	offset = offsetIn-zoneOffset

	timeAt12 = datetime.strptime(timeSet, "%H:%M")+offset
	return timeAt12

