from flask import Flask, send_from_directory
import ssl

app = Flask(__name__)

@app.route('/')
def index():
	return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    # Replace 'path/to/your/cert.pem' and 'path/to/your/key.pem' with your certificate and private key paths.
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)