from flask import Flask, render_template, request
import pandas as pd
import joblib

#Flask App

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

#Loading Trained Model

model = joblib.load("engagement_model.pkl")

MODEL_NAME = "Random Forest Regressor"
MODEL_ACCURACY = "75.5%"


#Home
@app.route("/")
def home():
    return render_template("index.html")

#Prediction

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Read Form Data
        gender = request.form.get("user_gender")
        age = int(request.form.get("user_age"))

        followers = int(request.form.get("followers_count"))
        following = int(request.form.get("following_count"))

        verified = request.form.get("is_verified") == "Yes"

        location = request.form.get("location")
        topic = request.form.get("topic")

        content_length = int(request.form.get("content_length"))

        hashtags = request.form.get("hashtags", "")

        hashtag_count = len([
            tag for tag in hashtags.split()
            if tag.startswith("#")
        ])

        has_media = request.form.get("has_media") == "Yes"

        device = request.form.get("device")
        language = request.form.get("language")

        likes = int(request.form.get("likes"))
        comments = int(request.form.get("comments"))
        shares = int(request.form.get("shares"))

        #Creating DataFrame

        input_df = pd.DataFrame([{
            "user_gender": gender,
            "user_age": age,
            "followers_count": followers,
            "following_count": following,
            "is_verified": verified,
            "location": location,
            "topic": topic,
            "content_length": content_length,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "hashtag_count": hashtag_count,
            "has_media": has_media,
            "device": device,
            "language": language
        }])

        # Predicton

        prediction = model.predict(input_df)[0]
        prediction_percentage = round(float(prediction) * 100, 2)

        #Progress Bar
        progress = min((prediction_percentage / 10) * 100, 100)


        #Engagement Level
        if prediction_percentage < 3:

            level = "Low Engagement"
            color_class = "low"

            tips = [
                "Use more relevant hashtags.",
                "Include an image or short video.",
                "Post during peak audience hours."
            ]

        elif prediction_percentage < 6:

            level = "Medium Engagement"
            color_class = "medium"
            tips = [
                "Add trending hashtags.",
                "Improve caption quality.",
                "Increase interaction with followers."
            ]

        else:

            level = "High Engagement"
            color_class = "high"
            tips = [
                "Excellent engagement expected.",
                "Your content is well optimized.",
                "Continue using this strategy."
            ]

        #Returning Result
        return render_template(
            "index.html",
            prediction=prediction_percentage,
            progress=progress,
            level=level,
            color_class=color_class,
            tips=tips,
            model_name=MODEL_NAME,
            accuracy=MODEL_ACCURACY
        )

    except Exception as e:
        print("Prediction Error:", e)

        return render_template(
            "index.html",
            error=str(e)
        )

#App run
if __name__ == "__main__":
    app.run(debug=True)