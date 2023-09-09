from datetime import datetime

@app.route('/api')
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get the current day dynamically
    current_day = datetime.utcnow().strftime('%A')

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,  # Dynamically getting the current day
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/username/repo",
        "status_code": 200
    }

    return jsonify(response_data)
