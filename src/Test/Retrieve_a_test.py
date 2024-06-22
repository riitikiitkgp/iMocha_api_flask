@app.route('/tests/<int:test_id>', methods=['GET'])
def get_test_details(test_id):
    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MOCHA_API_KEY}"
    }

    # Make the API request to iMocha
    response = requests.get(
        f"{API_BASE_URL}/tests/{test_id}",
        headers=headers
    )

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    elif response.status_code == 401:
        return jsonify(response.json()), 401
    else:
        return jsonify({"error": "Failed to retrieve test details", "details": response.text}), response.status_code