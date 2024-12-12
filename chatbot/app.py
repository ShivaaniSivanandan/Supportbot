<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import json
import csv
from datetime import datetime

# Initializing the Flask application
app = Flask(__name__, template_folder="templates")

# Loading the fine-tuned model and tokenizer from the specified directory
model_dir = "C:/Projects/chatbot/fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

# Creating a text classification pipeline using the fine-tuned model and tokenizer
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# Loading label-to-intent mappings from the model's configuration
id2label = model.config.id2label
label2id = {v: k for k, v in id2label.items()}  # Reverse mapping for lookup

# Loading predefined responses from a JSON file
try:
    with open("C:/Projects/chatbot/chatbot/responses.json", "r") as f:
        responses = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    responses = {}
    print("Warning: responses.json not found or malformed. Defaulting to empty.")

# Function to log user queries and predictions into a CSV file
def log_user_query(user_message, intent, confidence):
    with open("query_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user_message, intent, confidence])

# Route to serve the main chatbot interface
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for handling chat messages from the user
@app.route("/chat", methods=["POST"])
def chat():
    # Parsing JSON data from the request
    data = request.json    
    if not data or "message" not in data:
        return jsonify({"error": "Invalid input. Please provide a message."}), 400

    # Extracting and cleaning the user message
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message received."}), 400

    # Generating intent prediction using the classifier pipeline
    classification = classifier(user_message)
    label = classification[0]['label']  # e.g., "LABEL_0", "LABEL_1", etc.
    confidence = round(classification[0]['score'], 2)  # Confidence score (0–1)

    # Handling low-confidence predictions
    if confidence < 0.5:
        return jsonify({"response": "I'm not sure how to help with that. Could you rephrase your question?", "confidence": confidence})

    # Mapping the predicted label to the intent ID
    intent_id = label2id.get(label)
    if intent_id is None:
        return jsonify({"response": "I'm sorry, I don't understand your request.", "confidence": confidence})

    # Fetching the predefined response based on the predicted intent
    bot_response = responses.get(str(intent_id), "I'm sorry, I don't understand your request.")

    # Logging the query, intent, and confidence
    log_user_query(user_message, label, confidence)

    # Returning the bot's response and confidence score
    return jsonify({"response": bot_response, "confidence": confidence})

# API endpoint for handling user feedback
@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    user_feedback = data.get("feedback", "").strip()
    if not user_feedback:
        return jsonify({"error": "Feedback cannot be empty"}), 400

    # Appending user feedback to a log file
    with open("feedback.log", "a") as log_file:
        log_file.write(f"Feedback: {user_feedback}\n")

    return jsonify({"message": "Feedback received successfully!"})

# Starting the Flask application
if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import json
import csv
from datetime import datetime

# Initializing the Flask application
app = Flask(__name__, template_folder="templates")

# Loading the fine-tuned model and tokenizer from the specified directory
model_dir = "C:/Projects/chatbot/fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

# Creating a text classification pipeline using the fine-tuned model and tokenizer
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# Loading label-to-intent mappings from the model's configuration
id2label = model.config.id2label
label2id = {v: k for k, v in id2label.items()}  # Reverse mapping for lookup

# Loading predefined responses from a JSON file
try:
    with open("C:/Projects/chatbot/chatbot/responses.json", "r") as f:
        responses = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    responses = {}
    print("Warning: responses.json not found or malformed. Defaulting to empty.")

# Function to log user queries and predictions into a CSV file
def log_user_query(user_message, intent, confidence):
    with open("query_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user_message, intent, confidence])

# Route to serve the main chatbot interface
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for handling chat messages from the user
@app.route("/chat", methods=["POST"])
def chat():
    # Parsing JSON data from the request
    data = request.json    
    if not data or "message" not in data:
        return jsonify({"error": "Invalid input. Please provide a message."}), 400

    # Extracting and cleaning the user message
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message received."}), 400

    # Generating intent prediction using the classifier pipeline
    classification = classifier(user_message)
    label = classification[0]['label']  # e.g., "LABEL_0", "LABEL_1", etc.
    confidence = round(classification[0]['score'], 2)  # Confidence score (0–1)

    # Handling low-confidence predictions
    if confidence < 0.5:
        return jsonify({"response": "I'm not sure how to help with that. Could you rephrase your question?", "confidence": confidence})

    # Mapping the predicted label to the intent ID
    intent_id = label2id.get(label)
    if intent_id is None:
        return jsonify({"response": "I'm sorry, I don't understand your request.", "confidence": confidence})

    # Fetching the predefined response based on the predicted intent
    bot_response = responses.get(str(intent_id), "I'm sorry, I don't understand your request.")

    # Logging the query, intent, and confidence
    log_user_query(user_message, label, confidence)

    # Returning the bot's response and confidence score
    return jsonify({"response": bot_response, "confidence": confidence})

# API endpoint for handling user feedback
@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    user_feedback = data.get("feedback", "").strip()
    if not user_feedback:
        return jsonify({"error": "Feedback cannot be empty"}), 400

    # Appending user feedback to a log file
    with open("feedback.log", "a") as log_file:
        log_file.write(f"Feedback: {user_feedback}\n")

    return jsonify({"message": "Feedback received successfully!"})

# Starting the Flask application
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 4f10d78437bf31c0feec612c4720144541ce9436
