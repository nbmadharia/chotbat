Chotbat: AI-Powered Log and XML Analyzer

Chotbat is an AI-powered tool designed to analyze log and XML files dynamically using natural language prompts. It enables users to upload files, ask queries like "How many debug entries are in the logs?" or "What errors occurred between specific timestamps?", and receive precise answers powered by AI and custom logic.

Features

AI-Powered Analysis:
Understand natural language queries using NLP and dynamically respond.
Multi-File Support:
Analyze log and XML files.
Query Examples:
"How many debug entries are in the logs?"
"Are there any errors between 7:52:05 and 7:52:09?"
"What are the errors in the logs?"
User-Friendly Web Interface:
Upload files and interact via a simple web UI.
Time Range Analysis:
Extract and analyze log entries based on specific timestamps.
Installation

Prerequisites
Python 3.9 or higher installed on your system.
pip to manage Python dependencies.
Setup
Clone the repository:
git clone https://github.com/your-username/chotbat.git
cd chotbat
Install dependencies:
pip install -r requirements.txt
Start the Flask application:
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/
Usage

Upload a log or XML file via the web interface.
Enter a natural language query in the text box. Examples:
"How many debug entries are in the logs?"
"Log entries between 7:52:05 and 7:52:09."
"What errors occurred in the logs?"
View the analysis results below the form.
File Structure

chotbat/
│
├── app.py                    # Main Flask application
├── logs/                     # Directory to store uploaded log files
├── templates/                # HTML templates for the web interface
│   └── index.html            # Main HTML file for the UI
├── utils/                    # Utility functions for log processing
│   ├── __init__.py           # Makes utils a package
│   └── log_utils.py          # Log preprocessing and query handling
└── requirements.txt          # List of Python dependencies
Technologies Used

Python: Backend processing.
Flask: Web framework for the UI.
Transformers: NLP model for query understanding.
HTML/CSS: Frontend for file upload and interaction.
Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create a feature branch:
git checkout -b feature-name
Commit your changes:
git commit -m "Add some feature"
Push to your branch:
git push origin feature-name
Open a Pull Request.
License

This project is licensed under the MIT License.

Contact

Author: Your Name
Email: your-email@example.com
