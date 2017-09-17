from lxml import html
from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime as dt
from calendar import monthrange
import calendar
import requests

app = Flask(__name__)


@app.route("/<param>", methods=['GET'])
def get_sport_schedules(param):
    list_of_games = []
#     print(param)
#     page = requests.get('http://www.ucirvinesports.com/sports/m-baskbl/2016-17/schedule')
#     page = requests.get('http://www.ucirvinesports.com/sports/m-basebl/2016-17/schedule')
#     page = requests.get('http://www.ucirvinesports.com/sports/m-soccer/2016-17/schedule')
    
#     page = requests.get('http://www.ucirvinesports.com/sports/w-baskbl/2016-17/schedule')
#     page = requests.get('http://www.ucirvinesports.com/sports/w-track/2016-17/schedule')
    url = 'http://www.ucirvinesports.com/sports/' + param + '/2016-17/schedule'
    print(url)
    page = requests.get(url)
    
    
    tree = html.fromstring(page.content)
    
    
    dates = tree.xpath('//td[@colspan="6" or @class="e_date"]/text()')

    opponents = tree.xpath('//span[@class="team-name"]/text()')
#     opponents = tree.xpath('//span[@class="e_team e_opponent_name e_home"]/text() | //span[@class="e_teamname e_opponent_name"]/text()')
    locations = tree.xpath('//td[@class="e_notes"]/text()')
    scores = tree.xpath('//td[@class="e_result"]/text()')
    times = tree.xpath('//td[@class="e_status"]/text()')
    print("dates", dates)
    print("opponents", opponents)
    print("locations", locations)
    print("scores", scores)
    print("times", times)
    
    if param == "w-track":
        opponents = tree.xpath('//span[@class="e_teamname e_opponent_name e_home" or @class="e_teamname e_opponent_name"]/text()')
    
    for i in dates:
        if i == "\xa0":
            dates.remove(i)
        
    
    current_month = ""
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    
    now = dt.now()
    for i in range(len(scores)):
        if dates[i].lower() in months:
            current_month = dates[i]
            dates = dates[0:i] + dates[i+1:]
    
        cur_day = dates[i].strip().split(" ")[-1]
        if (dates[i].strip().split(" ")[-1] == ""):
            cur_day = dates[i-1].strip().split(" ")[-1]
            
        dict = {
    
            "month": current_month,
            "date": str(list(calendar.month_name).index(current_month))+ "/" + cur_day + "/" + str(now.year),
            "opponent": opponents[i],
            "location": locations[i],
            "score": scores[i].strip(),
            "time": times[i].strip()
        }
        
        list_of_games.append(dict)

    return jsonify(data=list_of_games)

if __name__ == "__main__":
#     app.run(debug=True)
    app.run(host='0.0.0.0')