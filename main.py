from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Handle file uploads
    for i in range(1, 5):
        file_key = f'file{i}'
        uploaded_file = request.files[file_key]
        if uploaded_file:
            # Save the file or process it as needed (adding file path to a list for now)
            uploaded_file.save(uploaded_file.filename)

    return jsonify({'message': 'Success!!'}), 200

if __name__ == '__main__':
    app.run(debug=True)