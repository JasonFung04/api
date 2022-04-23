
import json
import flask
from flask import request, jsonify
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
answers = [
    {'id': 0,
     '问题分类': '闲聊意图',
     '预测答案': '你好呀',
     },
    {'id': 1,
     '问题分类': '询问故障',
     '预测答案': '这个故障的解决方法是。 。 。 ',
     },
    {'id': 2,
     '问题分类': '查询信息',
     '预测答案': '这个信息是。 。 。 ',
     },
]
 
 
@app.route('/', methods=['GET'])
def home():
    return '''<h1>回答字典</h1>
<p>A prototype API for responding the question.</p>'''
 
 
@app.route('/api/answer/all', methods=['GET'])
def api_all():
    return jsonify(answers)
 
 
@app.route('/api/answer', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
 
    # Create an empty list for our results
  
    results = json.dumps(answers,ensure_ascii=False)
    
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for answer in answers:
        if answer['id'] == id:
            results.append(answer)
 
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


 
app.run()