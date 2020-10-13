from flask import *
from flask_restful import *
from datetime import date
import wikipedia
import datetime
import random
import wolframalpha
app=Flask(__name__)
api=Api(app)
class Welcome(Resource):
    def get(self):
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            return jsonify({'ISSAC':"Welcome Sir",
                            'GREETING':"Good Morning"})

        if currentH >= 12 and currentH < 18:
            return jsonify({'ISSAC':"Welcome Sir",
                            'GREETING':"Good Afternoon"})

        if currentH >= 18 and currentH !=0:
            return jsonify({'ISSAC':"Welcome Sir",
                            'GREETING':"Good Evening"})
class Question(Resource):
    def get(self,ques):
        query=ques
        client = wolframalpha.Client('AGVT22-AE67Q6APHU')
        try:
            try:
                 res = client.query(query)
                 results = next(res.results).text
                 return jsonify({'Question ':ques,
                                 'ISSAC ' : results})
                    
            except:
                 results = wikipedia.summary(query, sentences=2)
                 return jsonify({'Question ':ques,
                                 'ISSAC ' : results})
        
        except:
                stMsgs = ['I don\' Know !\n', 'I don\'t Understand \n']
                return jsonify ({'ISSAC ': random.choice(stMsgs)})
@app.errorhandler(404)
def error(e):
    return jsonify ({'ISSAC ':"Wrong Request "})

api.add_resource(Welcome,'/')
api.add_resource(Question,'/issac/<ques>')

if __name__=="__main__":
    app.run(debug=True)
                        
