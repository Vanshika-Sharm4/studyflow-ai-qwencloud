from flask import Flask, request, jsonify
from flask_cors import CORS
from qwen_client import generate_study_material

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "StudyFlow AI backend is running"}

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    course_notes = data.get("course_notes", "")

    if not course_notes.strip():
        return jsonify({"error": "Please provide course notes."}), 400

    result = generate_study_material(course_notes)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5001)