# Social Media Engagement Predictor

A Machine Learning web application that predicts the expected engagement
rate of a social media post using a **Random Forest Regressor**. The
project combines a Flask backend with a modern HTML/CSS/JavaScript
frontend.

------------------------------------------------------------------------

## Features

-   Predicts engagement rate as a percentage
-   Displays Low, Medium, or High engagement level
-   AI-generated recommendations
-   Modern responsive user interface
-   Progress indicator
-   Random Forest regression model
-   Flask backend with real-time predictions

------------------------------------------------------------------------

## Tech Stack

### Machine Learning

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Joblib

### Backend

-   Flask

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Font Awesome

------------------------------------------------------------------------

## Project Structure

``` text
Social Media Predictor/
│
├── backend/
│   ├── app.py
│   └── engagement_model.pkl
│
├── dataset/
│   └── synthetic_social_media_engagement.csv
│
├── frontend/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       └── index.html
│
├── ml/
│   ├── train_model.py
│   └── check_dataset.py
│
└── README.md
```

------------------------------------------------------------------------

## Installation

1.  Clone the repository.

2.  Install dependencies:

``` bash
pip install -r requirements.txt
```

3.  Start the Flask application:

``` bash
cd backend
python app.py
```

4.  Open your browser:

```{=html}
<!-- -->
```
    http://127.0.0.1:5000

------------------------------------------------------------------------

## Workflow

1.  Load the dataset.
2.  Train the Random Forest Regressor.
3.  Save the trained model.
4.  Load the model in Flask.
5.  User submits post information.
6.  Predict engagement rate.
7.  Display engagement percentage and AI recommendations.

------------------------------------------------------------------------

## Input Features

-   Gender
-   Age
-   Followers
-   Following
-   Verification Status
-   Location
-   Topic
-   Language
-   Content Length
-   Media Included
-   Device
-   Hashtags
-   Expected Likes
-   Expected Comments
-   Expected Shares

------------------------------------------------------------------------

## Output

-   Predicted Engagement Percentage
-   Engagement Level
-   AI Recommendations

------------------------------------------------------------------------

## Future Improvements

-   Use real-world datasets
-   Explainable AI
-   Cloud deployment
-   User authentication
-   Multiple social media platforms

------------------------------------------------------------------------

## Author

**Muhammad Nasir**

Machine Learning Internship Project
