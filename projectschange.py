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

@app.route("/project/edit-by-name", methods=["PATCH"])
def edit_project_by_name():
    data = request.get_json()

    if not data or "İşin Adı" not in data or "fields_to_update" not in data:
        return jsonify({"error": "JSON must include 'İşin Adı' and 'fields_to_update'"}), 400

    işin_adı = data["İşin Adı"]
    update_fields = data["fields_to_update"]

    response = requests.patch(
        f"{SUPABASE_URL}/rest/v1/Projects?İşin%20Adı=eq.{işin_adı}",
        headers=headers,
        json=update_fields
    )

    try:
        resp_data = response.json()
    except Exception:
        resp_data = response.text

    if response.status_code in [200, 204]:
        return jsonify({"message": "Project updated successfully", "data": resp_data}), 200
    else:
        return jsonify({"error": resp_data}), response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


