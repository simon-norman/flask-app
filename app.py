from flask import Flask,abort,jsonify,request
import numpy as np
from sklearn.externals import joblib


my_model = joblib.load("./LM_33%_split_model.pkl")

#creating web service running on port 8000, answer POST requests
app = Flask(__name__)
@app.route("/api", methods=['POST'])

#prediction function
def make_predict():

    if request.method =='POST':
        try:
            print("PASSED 1" + request)
            #expecting user imput as a json file with a title 'volume'
            data = request.get_json()
            print("PASSED 2" + data)
            user_data=data["volume"]
            print("PASSED 3" + user_data)
            
        except ValueError:
            return jsonify("error text here")

        #return a single prediction and convert to json
        return jsonify(my_model.predict(user_data).tolist())

###second test version
    ###data=request.get_json(force=True)

   ### user_data = [data['volume']]
    ###predict_request = np.array(user_data)
    ### my_model = joblib.load("LM_33%_split_model.pkl")
   ### y=my_model(predict_request)
   ### output=[y[0]]

    ###return jsonify(results=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
