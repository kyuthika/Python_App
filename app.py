from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_message = None
    if request.method == "POST":
        name = request.form.get("name", "Guest")
        user_message = f"Hello, {name}! Your Flask app is live on Azure App Service."
    return render_template("index.html", message=user_message)

if __name__ == "__main__":
    app.run()
