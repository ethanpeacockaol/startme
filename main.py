from flask import Flask, send_from_directory
import ssl
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')  # Replace with your certificate paths
    app.run(host='0.0.0.0', port=8000, ssl_context=context, debug=True)
