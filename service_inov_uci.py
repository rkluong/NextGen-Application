from lxml import html
import requests
from lxml import html
from flask import *
import requests
import json
from datetime import datetime as dt
from calendar import monthrange

app = Flask(__name__)



#Service Innovation UCI
@app.route("/", methods=['GET'])
def innovate():
    url = 'http://innovation.uci.edu/events/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    now = dt.now();
    #date
    dates = tree.xpath('//*[@id]/h1/div/span/text()');
    dates = list(map(str.strip, dates));
    dates = [str(now.month)+ "/" + x.split(" ")[-1] + "/{}".format(now.year) for x in dates if x != '']
##    print(dates);
##    print(dates);


    #event titles
    titles = tree.xpath('//*[@id]/div[1]/h2/a/text()')
    titles = [s.encode('ascii', errors = 'ignore') for s in titles];
    titles = [s.decode() for s in titles];


    #Descriptions
    info = tree.xpath('//*[@id]/div[2]/div/text()')
    info = list(map(str.strip, info));
    info = (filter(None, info));
    info = [ s.encode('ascii' , errors = 'ignore') for s in info];
    info = [s.decode() for s in info];

    


    address = "The Cove @ UCI 5141 California Ave Irvine, CA 92617"

    master_list = [];

    for i in range(len(titles)):
        obj = {
            "title": titles[i].strip(),
            "date": dates[i].strip(),
            "location": address.strip(),
            "info": info[i].strip()
            }
        master_list.append(obj);
        

#     return json.dumps(master_list,  sort_keys=True, indent=4, separators=(',', ': '), default = dict);
    return jsonify(data = master_list)
    
if __name__ == "__main__":
    app.run(debug=True);
        
