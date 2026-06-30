from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/v_data', methods=['GET'])
def primes():
    return jsonify({ 
        "vehicles":[
           {
            "TaskID":"264e---",
            "Duration":1,
            "Impact":5
           }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True,port=8050)
    

