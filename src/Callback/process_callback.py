@app.route('/callbacks/process', methods=['POST'])
def process_callbacks():
    request_data = request.json

    # Check if 'test_invitation_Ids' is present in the request body
    if 'test_invitation_Ids' not in request_data:
        return jsonify({'error': 'test_invitation_Ids is required'}), 400

    test_invitation_Ids = request_data['test_invitation_Ids']

    if not isinstance(test_invitation_Ids, list):
        return jsonify({'error': 'test_invitation_Ids must be a list of integers'}), 400

    # Check if there are any test_invitation_Ids to process
    if not test_invitation_Ids:
        return jsonify({'error': 'No test_invitation_Ids provided'}), 400

    # Process a maximum of 100 test_invitation_Ids at a time
    chunk_size = 100
    for i in range(0, len(test_invitation_Ids), chunk_size):
        chunk = test_invitation_Ids[i:i + chunk_size]
        # Process the chunk of test_invitation_Ids here

        # Simulated processing for demonstration
        processed_ids = chunk

        # Log the processed test_invitation_Ids
        print("Processed test_invitation_Ids:", processed_ids)

    # Return success response
    return jsonify({'result': {'test_invitation_Ids': {'successful': test_invitation_Ids, 'failed': []}}, 'errors': None})