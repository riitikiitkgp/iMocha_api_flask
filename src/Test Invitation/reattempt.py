@app.route('/invitations/<int:test_invitation_id>/reattempt', methods=['POST'])
def reattempt_test(test_invitation_id):
    # Get reattempt details from the request
    start_date_time = request.json.get('StartDateTime')
    end_date_time = request.json.get('EndDateTime')
    time_zone_id = request.json.get('TimeZoneId')
    callback_url = request.json.get('CallbackUrl')
    redirect_url = request.json.get('RedirectUrl')
    hide_instruction = request.json.get('hideInstruction', 0)
    send_email = request.json.get('sendEmail', 'no')

    # Prepare the request payload
    payload = {
        "StartDateTime": start_date_time,
        "EndDateTime": end_date_time,
        "TimeZoneId": time_zone_id,
        "CallbackUrl": callback_url,
        "RedirectUrl": redirect_url,
        "hideInstruction": hide_instruction,
        "sendEmail": send_email
    }

    # Remove None values from the payload
    payload = {k: v for k, v in payload.items() if v is not None}

    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MOCHA_API_KEY}"
    }

    # Make the API request to iMocha
    response = requests.post(
        f"{API_BASE_URL}/invitations/{test_invitation_id}/reattempt",
        json=payload,
        headers=headers
    )

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    elif response.status_code == 400:
        return jsonify(response.json()), 400
    else:
        return jsonify({"error": "Failed to allow reattempt", "details": response.text}), response.status_code