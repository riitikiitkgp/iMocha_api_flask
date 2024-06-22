@app.route('/invitations/<int:test_invitation_id>/cancel', methods=['POST'])
def cancel_invitation(test_invitation_id):
    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MOCHA_API_KEY}"
    }

    # Make the API request to iMocha
    response = requests.post(
        f"{API_BASE_URL}/invitations/{test_invitation_id}/cancel",
        headers=headers
    )

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    elif response.status_code == 400:
        return jsonify(response.json()), 400
    else:
        return jsonify({"error": "Failed to cancel invitation", "details": response.text}), response.status_code