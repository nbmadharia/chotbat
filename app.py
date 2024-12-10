from flask import Flask, request, render_template, jsonify
import os
from utils.log_utils import preprocess_logs, analyze_query_with_nlp, execute_task

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './logs'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form.get('query')
    uploaded_file = request.files.get('file')

    if not query or not uploaded_file:
        return jsonify({"error": "Please provide a query and upload a log file."}), 400

    # Save uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
    uploaded_file.save(file_path)

    # Process query
    with open(file_path, 'r') as file:
        log_data = file.readlines()

    structured_logs = preprocess_logs(log_data)
    intent, entities = analyze_query_with_nlp(query, log_data)
    response = execute_task(intent, entities, structured_logs)

    return jsonify({"query": query, "response": response})

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
