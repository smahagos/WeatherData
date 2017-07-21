import requests
import json
import time
import datetime

def get_weather_data(city):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=66b5fce51ffe0e5dc4493cdc0c28f12c" % (city))
    if response.status_code == 200:
    #print(response.status_code)
        data = json.loads(response.text)
        return data
    else:
        return  None
#def get_weather_data_by_coordinates()
#    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=f5dda084e3a31d89a4975204baaa6559" % (city))
 #   if response.status_code == 200:
  #  print(response.status_code)
   # data = json.loads(response.text)
    #return data
 #else:
  #  return  None
def post_weather_data_to_stream(lat , lon , temperature , windspeed , humidity , clouds):
    id ="RM44YzYqmjHqv5d1o2JQ"
    key="lzNNgrgpvXFRyKDG7xNW"
    #url = "https://data.sparkfun.com/input/%s?private_key=%s&location=%s&temp=%f&windspeed=%f"
    url = "https://data.sparkfun.com/input/%s?private_key=%s&clouds=%f&collection_time=%s&humidity=%f&kentid=%s&lat=%f&lon=%f&temperature=%f&windspeed=%f"
    collection_time = str(datetime.datetime.now())
    kentid = "smahagos"
    response = requests.get(url % (id,key,clouds,collection_time,humidity,kentid,lat,lon,temperature,windspeed))
    print(response.status_code)

def stream_weather_data(location):
    data = get_weather_data(location)
    print(data)
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    temperature = data['main']['temp'] - 273
    humidity = data['main']['humidity']
    windspeed = data['wind']['speed']
    clouds = data['clouds']['all']
    post_weather_data_to_stream(lat , lon , temperature , windspeed , humidity , clouds)

for i in range(1,11):
    print(i)
    stream_weather_data("Columbus,OH")
    time.sleep(10)
    print("complete")
#print(get_weather_data("Cleveland,OH"))
#print(get_weather_data_by_coordinates("Chicago"))

#for i in range(1,11):
#    post_weather_data_to_stream("Cleveland,OH",i+20,i+30)
#    print("done with #%d" % i)
#    print("Complete")

#id ="aGDX02EMLwFEpXW1X8DK"
#key="KEjmAM9JpVUGMjWRjEa5"
#url = "https://data.sparkfun.com/input/%s?private_key=%s&location=%s&temp=%d&windspeed=%d"
#for i in range(1,11):
#    response = requests.get(url % (id,key,"Cleveland",0,0))
#    print("done %d" % i,response.status_code)
#print("complete")