@app.route('/tests', methods=['GET'])
def get_tests_list():
    # Get query parameters
    page_no = request.args.get('pageNo', 1)
    page_size = request.args.get('pageSize', 100)
    labels_filter = request.args.get('labelsFilter')
    status = request.args.get('status')

    # Prepare query parameters
    params = {
        'pageNo': page_no,
        'pageSize': page_size
    }
    if labels_filter:
        params['labelsFilter'] = labels_filter
    if status:
        params['status'] = status

    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Make the API request to iMocha
    response = requests.get(
        f"{API_BASE_URL}/tests",
        params=params,
        headers=headers
    )

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    elif response.status_code == 400:
        return jsonify(response.json()), 400
    else:
        return jsonify({"error": "Failed to retrieve tests list", "details": response.text}), response.status_code