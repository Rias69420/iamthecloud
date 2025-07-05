from flask import Flask, request, abort

app = Flask(__name__)

UPLOAD_TOKEN = "aM#nYCc>R>oV:tqZxmk$"
LOG_SAVE_PATH = "/tmp/received_logs.txt"  # Use temp storage on Vercel

@app.route('/upload', methods=['POST'])
def upload_log():
    token = request.args.get('token')
    if token != UPLOAD_TOKEN:
        abort(403)
    log_data = request.form.get('log')
    if not log_data:
        return "No log data", 400
    with open(LOG_SAVE_PATH, "a", encoding="utf-8") as f:
        f.write(log_data + "\n---\n")
    return "Log received", 200

if __name__ == '__main__':
    app.run()
