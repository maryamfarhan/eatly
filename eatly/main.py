from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Meal Recommendation Page/Ask Page
@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")
    
@app.route("/ask_page")
def ask_page():
    return render_template("ask_page.html")

# Community / Feed Page
@app.route("/community")  # When user visits /community
def community():

    return render_template("community.html")


# Request a Home-Cooked Meal (Optional)

# About / Contact (Optional)
@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)




