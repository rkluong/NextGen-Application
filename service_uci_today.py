from webcrawler import Spider

from datetime import datetime as dt
from calendar import monthrange
from flask import Flask
from flask import jsonify
import requests
import json

app = Flask(__name__);
 
@app.route("/", methods=['GET'])
def process():
    titles = []
    time = []
    descriptions = []
    location = []
    date = []
    now = dt.now()
    #iterate from current day to the last day of the Month
    for i in range(now.day, now.day+10):
        url = 'https://today.uci.edu/calendar/day/2017/'+ str(now.month) + '/' + str(i)
        crawler = Spider(url)
        
        #Titles
        crawler.parse('//h3/a/text()')
        titles += crawler.get_info()[1:]
        
        #Locations
        crawler.parse('//*[@id]/div/div[3]/div[1]/div[2]/a/text()')
        location += crawler.get_info();
        

        #time
        crawler.parse('//*[@id]/div/div[3]/div[1]/div[1]/abbr/text()')
        time += crawler.get_info();

        #Event Description
        crawler.parse('//*[@id]/div/h4/text()')
        descriptions += crawler.get_info();

        #Date
        for k in range(len(crawler.get_info())):
            date.append(now.strftime('%d') + "/{}/{}".format(i, now.year))
        
        for i in range(len(titles)):
            if titles[i] == 'Striking a Balance: Conservation and...':
                time.insert(i, 'x')
        
    master_list = []
    ##print(len(location), len(titles), len(time), len(descriptions));
    titles = [ s.encode('ascii' , errors = 'ignore') for s in titles];
    titles = [s.decode().replace('\"', '') for s in titles];
    # print(titles);
    descriptions = [ s.encode('ascii' , errors = 'ignore') for s in descriptions];
    descriptions = [s.decode().replace('\n', '') for s in descriptions];
    lowest = min(len(location), len(titles), len(time), len(descriptions))
    for i in range(lowest):
        dicti = {
            "location": location[i].strip(),
            "time": time[i].strip(),
            "info": descriptions[i].strip(),
            "date": date[i].strip(),
            "title": titles[i].strip()
            }
        master_list.append(dicti)
   
#     return json.dumps(master_list,  sort_keys=True, indent=4, separators=(',', ': '), default = dict);
    return jsonify(data = master_list)

# process();
if __name__ == '__main__':
    app.run(debug=True)
##    run(host = '127.0.0.1', port = 5000);
    # app.run(host = '127.0.0.1', port = 5001,debug=True)
    
    

