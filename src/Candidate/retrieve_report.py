@app.route('/reports/<int:test_invitation_id>', methods=['GET'])
def retrieve_test_report(test_invitation_id):
    url = f"https://apiv3.imocha.io/v3/reports/{test_invitation_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve test report"}), response.status_code