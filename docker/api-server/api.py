from flask import Flask, request, jsonify
from ai_engine import AICodeGenerator  # Import AI engine

app = Flask(__name__)
ai = AICodeGenerator()

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt")
    code = ai.generate_code(prompt)
    return jsonify({"code": code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
