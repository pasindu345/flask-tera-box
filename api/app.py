from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Requests

# Terabox URL Extract Function
def get_terabox_download_url(terabox_url):
    try:
        match = re.search(r'/s/([a-zA-Z0-9]+)', terabox_url)
        if not match:
            return None
        
        file_id = match.group(1)
        download_url = f"https://terabox-api.example.com/get?file_id={file_id}"  # Update this part
        
        return download_url
    except:
        return None

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    
    if not url:
        return jsonify({
            "status": "error",
            "message": "No URL provided",
            "join": "https://t.me/sl_bjs",
            "support": "@Pasindu_21"
        }), 400

    download_url = get_terabox_download_url(url)

    if download_url:
        return jsonify({
            "status": "success",
            "url": download_url
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid Terabox URL",
            "join": "https://t.me/sl_bjs",
            "support": "@Pasindu_21"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
