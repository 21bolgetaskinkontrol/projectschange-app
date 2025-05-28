from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

url = "https://whmkswmgdtneqcpcjwtk.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndobWtzd21nZHRuZXFjcGNqd3RrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0ODI0MDk2MCwiZXhwIjoyMDYzODE2OTYwfQ.XLbdNl01_g-HYr7MQRlfAWfYARyni8XIflI98d5mug0"

supabase: Client = create_client(url, key)

@app.route('/update_project', methods=['POST'])
def update_project():
    try:
        data = request.get_json()
        id = data.get("id", "1")
        print(data)
        data_without_id = {k: v for k, v in data.items() if k != "id"}
        response = supabase.table("Projects").update(data_without_id).eq("id", id ).execute()

        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
