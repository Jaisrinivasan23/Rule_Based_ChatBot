from flask import Flask, request, jsonify, render_template
import spacy
import json

app = Flask(__name__)

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Load data from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")


# Route to handle user queries
@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    query = data["query"]
    response = generate_response(query)
    return jsonify({"response": response})

# Function to generate response based on user query
def generate_response(query):
    doc = nlp(query.lower())  # Process query text with spaCy
    response = ""

    # Check for keywords in the query and generate response accordingly
    if any(token.text in ["address", "location"] for token in doc):
        response = data["address"]
    elif "hi" in query:
        response = data["Hello"]
    elif any(token.text in ["email", "email address"] for token in doc):
        response = data["email"]
    elif "contact number" in query:
        response = data["contact_number"]
    elif "about school" in query:
        response = data["about_school"]
    elif "infrastructure" in query:
        response = data["infrastructure"]
    elif "color dress" in query:
        response = data["color_dress"]
    elif "admission process" in query:
        if "montessori" in query:
            response = data["admission_process_montessori"]
        else:
            response = data["admission_process_grade"]
    elif "selection procedure" in query:
        response = data["selection_procedure"]
    elif "application form" in query:
        response = data["application_form"]
    elif "documents needed" in query:
        response = data["required_documents"]
    elif "fee policy" in query:
        response = data["fee_policy"]
    elif "registration fee" in query:
        response = data["registration_fee"]
    elif "installments" in query:
        response = data["installments"]
    else:
        response = "I'm sorry, I couldn't understand your query. Please try again."

    return response

if __name__ == "__main__":
    app.run(debug=True)
