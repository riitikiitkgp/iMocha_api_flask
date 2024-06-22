@app.route('/tests/<int:test_id>/testlinks/<int:test_link_id>/invite', methods=['POST'])
def invite_candidate_by_test_link(test_id, test_link_id):
    # Candidate details from the request
    candidate_email = request.json.get('email')
    candidate_name = request.json.get('name')
    
    # Additional optional parameters
    callback_url = request.json.get('callbackUrl')
    redirect_url = request.json.get('redirectUrl')
    disable_mandatory_fields = request.json.get('disableMandatoryFields', 0)
    hide_instruction = request.json.get('hideInstruction', 0)
    send_email = request.json.get('sendEmail', 'no')

    # Prepare the request payload
    payload = {
        "email": candidate_email,
        "name": candidate_name,
        "callbackUrl": callback_url,
        "redirectUrl": redirect_url,
        "disableMandatoryFields": disable_mandatory_fields,
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
        f"{API_BASE_URL}/tests/{test_id}/testlinks/{test_link_id}/invite",
        json=payload,
        headers=headers
    )

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    
    else:
        return jsonify({"error": "Failed to invite candidate", "details": response.text}), response.status_code