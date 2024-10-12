from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace this URL with your preferred IP geolocation service
GEOLOCATION_API_URL = "https://ipinfo.io/{}/json"

@app.route("/")
def index():
    # Get the IP address of the user
    ip_address = request.remote_addr if request.remote_addr != "127.0.0.1" else "YOUR_PUBLIC_IP"
    
    # Fetch geolocation data based on the IP address
    response = requests.get(GEOLOCATION_API_URL.format(ip_address))
    data = response.json()

    # Extract necessary geolocation details (latitude, longitude)
    location = data.get("loc", "0,0").split(",")
    latitude, longitude = location if len(location) == 2 else (0, 0)

    return render_template("index.html", latitude=latitude, longitude=longitude, ip=ip_address)

if __name__ == "__main__":
    app.run(debug=True)
