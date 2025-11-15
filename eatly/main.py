from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Meal Recommendation Page/Ask Page
@app.route("/recommendations", methods=["GET", "POST"])
def recommendations():
    
    # Shows the user a form to help develop the prompt to send the Eatly AI
    
    if request.method == "GET":
        return render_template("ask_page.html")

    # Until the AI is directly called in via an API, hard-code and run the prompt through manually
    if request.method == "POST":
        data = request.values 
        
        cravings = data.get("cravings", "None")
        available_ingredients = data.get("available_ingredients", "None")
        preference_lifestyle = data.get("preference_lifestyle", "None")
        avoid_foods = data.get("avoid_foods", "None")
        preferred_cook_time = data.get("preferred_cook_time", "None")
        loved_cuisines = data.get("loved_cuisines", "None")
        disliked_foods = data.get("disliked_foods", "None")
        available_tools = data.get("available_tools", "None")
        number_of_meals = data.get("number_of_meals", "None")
        allowed_creativity = data.get("allowed_creativity", "None")
        
        print(
            f"Cravings: {cravings}", 
            f"Available Ingredients: {available_ingredients}", 
            f"Dietary Preference or Lifestyle: {preference_lifestyle}", 
            f"Allergies / Foods to Avoid: {avoid_foods}", 
            f"Cooking Time: {preferred_cook_time}", 
            f"Favorite Cuisines: {loved_cuisines}", 
            f"Disliked Cuisines/Ingredients: {disliked_foods}", 
            f"Kitchen Tools Available: {available_tools}", 
            f"Number of Meals to Plan For: {number_of_meals}", 
            f"Creativity Level: {allowed_creativity}")

        return render_template("recommendations.html")

@app.route("/ask_page", methods=["GET", "POST"])
def ask_page():
        
    return render_template("ask_page.html")

# Community / Feed Page
@app.route("/community")  # When user visits /community
def community():

    return render_template("community.html")

# Request a Home-Cooked Meal (Optional)

# About / Contact (Optional)


if __name__ == "__main__":
    app.run(debug=True)

