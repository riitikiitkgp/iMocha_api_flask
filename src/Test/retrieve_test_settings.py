@app.route('tests/<int:test_id>/settings', methods=['GET'])
def get_test_settings(test_id):
    api_url = f"https://apiv3.imocha.io/v3/tests/{test_id}/settings"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to retrieve test settings"}), response.status_code