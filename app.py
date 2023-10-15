from flask import Flask, render_template, request, redirect
from qrcode_scanner import scan_qr_code

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan_qr_code", methods=["GET", "POST"])

def scan_qr_code_route():
    # Handle file upload and QR code scanning here
    image = request.files['image']
    image.save("uploaded_image.png")

    # Call the scan_qr_code function and get the results
    result = scan_qr_code("uploaded_image.png")

    # Check if a URL was extracted from the QR code
    for qr_code_result in result:
        if isValidURL(qr_code_result):
            # If a valid URL is found, redirect to it
            return redirect(qr_code_result)

    return render_template("index.html", qr_code_result=result)

# Function to check if a string is a valid URL
def isValidURL(str):
    return str.startswith("http://") or str.startswith("https://") or str.startswith("")

if __name__ == "__main__":
    app.run(debug=True)
