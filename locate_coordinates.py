from flask import *
from flask_restful import *
from datetime import date
from geopy import Nominatim
import datetime
import wolframalpha
app=Flask(__name__)
api=Api(app)
class Welcome(Resource):
    def get(self):
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            return jsonify({'BRI-AGE':"Welcome Sir",
                            'GREETING':"Good Morning"})

        if currentH >= 12 and currentH < 18:
            return jsonify({'BRI-AGE':"Welcome Sir",
                            'GREETING':"Good Afternoon"})

        if currentH >= 18 and currentH !=0:
            return jsonify({'BRI-AGE':"Welcome Sir",
                            'GREETING':"Good Evening"})
class Question(Resource):
    def get(self,lat,lon):
	    coord=[]
	    coord.append(lat)
	    coord.append(lon)
        geolocator=Nominatim(user_agent="test/1")
        location =geolocator.reverse(f'{coord[0]},{coord[1]}')
	    s=location.address
     
     
     
        final=s.split(",")
        locatity=final[0]
        city=final[2]
        pincode=final[-2]
        state=final[-3]
        country=final[-1]
        query1="Average temperature of {}".format(city)
        query2="Average Humidity of {}".format(city)
        client = wolframalpha.Client('AGVT22-AE67Q6APHU')

        try:
            res = client.query(query)
            res2=client.query(query2)
            results = next(res.results).text
            results2 = next(res2.results).text

            return jsonify({'Latitute ':lat,
                            'Longitute ' : lon,
                            'Locality ':locality,
                            'City ':city,
                            'Pincode ':pincode,
                            'State ':state,
                            'Country ':country,
                            'Temperature ':results,
                            'Humidity ':results2 })
        except:
            return jsonify({'Latitute ':lat,
                            'Longitute ' : lon,
                            'Locality ':locality,
                            'City ':city,
                            'Pincode ':pincode,
                            'State ':state,
                            'Country ':country,
                            'Temperature ':"25 C",
                            'Humidity ':"40"})

@app.errorhandler(404)
def error(e):
    return jsonify ({'BRI-AGE ':"Sorry ! Wrong Request "})

api.add_resource(Welcome,'/')
api.add_resource(Question,'/query/<lat>,<lon>')

if __name__=="__main__":
    app.run(debug=True)
