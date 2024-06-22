@app.route('/tests/<int:test_id>/settings', methods=['POST'])
def update_test_settings(test_id):
    current_settings_response = requests.get(f"{API_BASE_URL}/{test_id}/settings")

    if current_settings_response.status_code != 200:
        return jsonify({"error": "Failed to fetch current test settings"}), current_settings_response.status_code

    current_settings = current_settings_response.json()

    new_settings = request.json
    updated_settings = current_settings.copy()
    updated_settings.update(new_settings)

    response = requests.post(f"{API_BASE_URL}/{test_id}/settings", json=updated_settings)
    return jsonify(response.json()), response.status_code