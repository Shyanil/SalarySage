# SalarySage

**SalarySage** is a salary prediction tool that estimates a candidate's potential monthly salary based on their years of experience, job title, and education level. It utilizes a simple linear regression model to make predictions and provides insights into expected salary ranges based on market conditions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Predicts monthly salary based on user input.
- Takes into account various factors like job title and education level.
- User-friendly API for integration with other applications.

## Gradient Descent Algorithm
This project employs the **Gradient Descent** algorithm for optimizing the linear regression model. 


## Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Matplotlib
- Seaborn

## How It Works

1. The user inputs their details, including name, job title, education level, and years of experience.
2. The application uses a linear regression model to calculate the predicted salary.
3. A response is generated providing the predicted salary and a brief explanation.

## API Documentation

### Endpoint

- `POST /predict`

#### Request Body

```json
{
    "name": "Shyanil Mishra",
    "job_title": "Data science engineer",
    "education_level": "Bachelor's",
    "years_of_experience": 1
}
```

```json

{
    "message": "Based on our prediction, the candidate Shyanil Mishra, a Data science engineer with an education level of Bachelor's and 1 years of experience, can expect a monthly salary of ₹35,000. This may vary based on company and market conditions."
}
```
## Clone the Repository

To clone this repository to your local machine, you can use the following command:

```bash
git clone https://github.com/Shyanil/SalarySage.git
```
Navigate to the project directory:
```bash
cd SalarySage
```
Run the Flask application:
```bash
python app.py
```
Use a tool like Postman to send a POST request to http://127.0.0.1:5000/predict.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

https://flask.palletsprojects.com/
https://numpy.org/doc/
https://pandas.pydata.org/docs/
https://matplotlib.org/stable/contents.html
https://seaborn.pydata.org/
