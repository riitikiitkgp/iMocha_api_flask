@app.route('/candidates/testattempts?state=completed', methods=['POST'])
def get_invites():
    try:
        data = request.get_json()
        start_datetime = data.get('StartDateTime')
        end_datetime = data.get('EndDateTime')

        # Check if required parameters are present
        if not start_datetime or not end_datetime:
            return jsonify({'errors': ['StartDateTime and EndDateTime are required']}), 400

        # Make request to iMocha API
        response = requests.post(API_URL+ "/candidates/testattempts?state=completed", json=data)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({'errors': ['Failed to retrieve invites']}), 500
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 500