from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/saved', methods=['GET'])
def save_to_text():
    url = request.args.get('url')
    
    if url:
        value_after_slash = url.split('/')[-1]
        with open('data.txt', 'a') as file:
            file.write(value_after_slash + '\n')
        return jsonify({'message': 'Data extracted and saved successfully'}), 200
    else:
        return jsonify({'error': 'URL parameter not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
