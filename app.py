from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from src.data_processing import load_and_process_data
from src.model import train_model, make_prediction

app = Flask(__name__)

# Load and train the model
data = load_and_process_data("data/public_transport_data.csv")
model = train_model(data) if data is not None else None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'Ошибка': 'Модель не загружена'}), 500

    try:
        # Get values from the form
        deviceid = float(request.form['deviceid'])
        direction = float(request.form['direction'])
        segment = float(request.form['segment'])
        length = float(request.form['length'])

        # Make a prediction
        predicted_seconds = make_prediction(model, deviceid, direction, segment, length)

        # Calculate arrival time based on the current time
        current_time = datetime.now()
        arrival_time = current_time + timedelta(seconds=predicted_seconds)
        formatted_arrival_time = arrival_time.strftime('%H:%M')

        return jsonify({'prediction': formatted_arrival_time})
    except ValueError:
        return jsonify({'Ошибка': 'Неправильный ввод данных'}), 400


if __name__ == '__main__':
    app.run(debug=True)
