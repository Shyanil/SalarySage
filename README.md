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
Copy code
{
    "message": "Based on our prediction, the candidate Shyanil Mishra, a Data science engineer with an education level of Bachelor's and 1 years of experience, can expect a monthly salary of ₹75,000. This may vary based on company and market conditions."
}
```

