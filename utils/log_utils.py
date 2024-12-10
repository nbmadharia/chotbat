import re
from datetime import datetime
from transformers import pipeline

# Initialize AI model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Preprocess log file
def preprocess_logs(log_lines):
    structured_logs = []
    for line in log_lines:
        match = re.match(r"\[(.*?)\]\s(\w+)\s-\s(.*)", line)
        if match:
            timestamp, level, message = match.groups()
            structured_logs.append({"timestamp": timestamp, "level": level, "message": message})
    print(f"Structured Logs: {structured_logs}")  # Debugging output
    return structured_logs


# Analyze query with NLP
def analyze_query_with_nlp(query, log_data):
    intent = None
    entities = {}

    # Recognize intents for counting entries
    if "how many" in query.lower():
        intent = "count"
        if "debug" in query.lower():
            entities["level"] = "DEBUG"
        elif "error" in query.lower():
            entities["level"] = "ERROR"

    # Recognize intent for checking specific errors
    elif "is there any error" in query.lower():
        intent = "search"
        timestamps = re.findall(r"\d{1,2}:\d{1,2}:\d{1,2}", query)
        entities["timestamps"] = timestamps

    # Recognize intent for filtering logs
    elif "log entries between" in query.lower():
        intent = "filter"
        timestamps = re.findall(r"\d{1,2}:\d{1,2}:\d{1,2}", query)
        entities["timestamps"] = timestamps

    # Recognize intent for listing errors
    elif "what are the errors" in query.lower():
        intent = "list_errors"

    return intent, entities

# Execute tasks dynamically
def execute_task(intent, entities, structured_logs):
    if intent == "count":
        level = entities.get("level", "")
        count = sum(1 for log in structured_logs if log["level"] == level)
        return f"There are {count} {level.lower()} entries in the logs."

    elif intent == "search":
        timestamps = entities.get("timestamps", [])
        if len(timestamps) == 2:
            start_time = datetime.strptime(timestamps[0], "%H:%M:%S")
            end_time = datetime.strptime(timestamps[1], "%H:%M:%S")
            filtered_logs = [
                log for log in structured_logs
                if start_time <= datetime.strptime(log["timestamp"].split()[1].split(",")[0], "%H:%M:%S") <= end_time
            ]
            error_logs = [log for log in filtered_logs if log["level"] == "ERROR"]
            return "Yes, there are error entries in the specified time range." if error_logs else "No errors found."

    elif intent == "filter":
        timestamps = entities.get("timestamps", [])
        if len(timestamps) == 2:
            start_time = datetime.strptime(timestamps[0], "%H:%M:%S")
            end_time = datetime.strptime(timestamps[1], "%H:%M:%S")
            filtered_logs = [
                log for log in structured_logs
                if start_time <= datetime.strptime(log["timestamp"].split()[1].split(",")[0], "%H:%M:%S") <= end_time
            ]
            if not filtered_logs:
                return "No log entries found in the specified time range."
            return {"filtered_logs": filtered_logs}

    elif intent == "list_errors":
        error_logs = [log for log in structured_logs if log["level"].upper() == "ERROR"]
        if error_logs:
            return {"error_entries": error_logs, "error_count": len(error_logs)}
        else:
            return "No errors found in the logs."


    return "I'm sorry, I couldn't process that request."
