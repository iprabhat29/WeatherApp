from flask import Flask, jsonify
import requests, json 
import string  
import datetime
from datetime import datetime,timedelta
from flask import abort
from server import *
import threading
import thread
print_lock = threading.Lock()

app = Flask(__name__)

"""
This function hits the werather api with the url and gets the response back.
The response is Jsonified.
"""
def urlopen(city_name):
  api_key = "062b3ebf1bb4453cc5a8773030ab9ae1"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  response = requests.get(complete_url,timeout = 5)
  if(response.status_code == 200):
    result_data = response.json()
  else:
    print response.status_code
  return result_data
"""
This function formats the data received by the web api.
"""
def data_organizer(raw_api_dict):
  data = dict(
  city=raw_api_dict.get('name'),
  country=raw_api_dict.get('sys').get('country'),
  temp=raw_api_dict.get('main').get('temp'),
  temp_max=raw_api_dict.get('main').get('temp_max'),
  temp_min=raw_api_dict.get('main').get('temp_min'),
  humidity=raw_api_dict.get('main').get('humidity'),
  pressure=raw_api_dict.get('main').get('pressure'),
  sky=raw_api_dict['weather'][0]['main'],
  wind=raw_api_dict.get('wind').get('speed'),
  wind_deg=raw_api_dict.get('deg'),
  cloudiness=raw_api_dict.get('clouds').get('all')
  )
  return data

"""
This function is called when a user sends get request
URL format for this API will be http://127.0.0.1:5000/weatherapi/<city_name>
"""
@app.route('/weatherapi/<string:location>', methods=['GET'])
def get_task(location):
  try:
    data_rcvd = data_organizer(urlopen(location))
    print "Sending back data from REST"
    return jsonify(data_rcvd)
  except IOError:
    print('no internet')

"""
This function starts the REST Service

"""

def rest_api_run():
  #print "Starting REST"
  app.run()

"""
When this program is run, it will spawn 2 threads:
1) This thread will be starting REST API.
2) This thread will start the sever which will spawn separate 
   thread for separate client
"""

if __name__ == '__main__':
  t1 = threading.Thread(target=Main, args=())
  t2 = threading.Thread(target=rest_api_run, args=())
  t1.start()
  t2.start()
