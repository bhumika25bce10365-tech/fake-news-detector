from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model/model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']
    
    # Convert input text
    vec = vectorizer.transform([news])
    
    # Predict
    result = model.predict(vec)[0]

    if result == 1:
        prediction = "Real News ✅"
    else:
        prediction = "Fake News ❌"

    return f"""
    <h2>Result: {prediction}</h2>
    <br><a href="/">Go Back</a>
    """

# Run app
if __name__ == "__main__":
    app.run(debug=True)