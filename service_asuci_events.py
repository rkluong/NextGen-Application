from lxml import html
from flask import Flask
from flask import request
from flask import jsonify
import requests
from datetime import datetime as dt
from calendar import monthrange

app = Flask(__name__)

months = {"Jan": "01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", 'Dec':'12'}

@app.route("/", methods=['GET'])
def get_asuci_events():
	list_of_events = []
	
	url = 'http://www.asuci.uci.edu/'
	page = requests.get(url)
	
	
	tree = html.fromstring(page.content)
	
	dates = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/h3/text()')
	locations = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/h4/a/text()')
	times = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/span/text()')
	links = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/h4/a/@href')
	eventDate = []
	
	for item in dates:
		dateInfo = item.split(' ')
		day = dateInfo[2][:-2] if len(dateInfo[2][:-2]) > 1 else '0' + dateInfo[2][:-2]
		dateStr = months[dateInfo[1]] + '/' + day + '/17'
		eventDate.append(dateStr)

	for i in range(len(dates)):	 
		dict = {
	 
			"date": dates[i].strip(),
			"location": locations[i],
			"time": times[i].strip(),
			"link": links[i].strip(),
			"eventDate": eventDate[i].strip()
		}
		 
		list_of_events.append(dict)

	return jsonify(data=list_of_events)


if __name__ == "__main__":
	app.run(debug=True)
#	 app.run(host='0.0.0.0', port = 5000)
