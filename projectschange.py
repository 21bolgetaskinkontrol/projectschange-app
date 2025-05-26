import requests
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SUPABASE_URL = 'https://whmkswmgdtneqcpcjwtk.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndobWtzd21nZHRuZXFjcGNqd3RrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0ODI0MDk2MCwiZXhwIjoyMDYzODE2OTYwfQ.XLbdNl01_g-HYr7MQRlfAWfYARyni8XIflI98d5mug0' 

headers = {
    'apikey': SUPABASE_API_KEY,
    'Authorization': f'Bearer {SUPABASE_API_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

@app.route("/project/update", methods=["POST"])
def update_project():
    project = request.get_json()
    if not project:
        return jsonify({"error": "JSON body missing"}), 400
    response = requests.post(
    f"{SUPABASE_URL}/rest/v1/Projects",
    headers=headers,
    json=project
)
    if response.status_code in [200, 201]:
        return jsonify({"message": "Project added successfully", "data": response.json()}), 201
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


