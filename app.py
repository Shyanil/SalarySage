from flask import Flask, request, jsonify
import math
from model_params import w, b

app = Flask(__name__)

def predict_salary(years_of_experience):
    # Calculate the predicted salary based on years of experience
    predicted_salary = w * years_of_experience + b
    
    # Round down the predicted salary using math.floor
    monthly_salary = math.floor(predicted_salary)
    
    return monthly_salary

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    name = data.get('name')
    job_title = data.get('job_title')
    education_level = data.get('education_level')
    years_of_experience = data.get('years_of_experience')

    try:
        # Ensure years_of_experience is a float
        years_of_experience = float(years_of_experience)

        # Call the prediction function
        monthly_salary = predict_salary(years_of_experience)
        
        # Create a beautiful response
        response = {
            'message': (
                f'Based on our prediction, the candidate {name}, a {job_title} '
                f'with an education level of {education_level} and {years_of_experience} years of experience, '
                f'can expect a monthly salary of ₹{monthly_salary:,}. This may vary based on company and market conditions.'
            )
        }
        
        return jsonify(response)

    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter numeric values for years of experience.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
