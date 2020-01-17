from flask import render_template, Flask

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """
    Returns  homepage template
    """

    return  render_template("home.html")


# Run if main file
if __name__ == "__main__":
    app.run(debug=True)
