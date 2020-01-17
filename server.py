from flask import render_template, Flask
import config

app = Flask(__name__, template_folder="templates")

# Get application instance
connex_app = config.connex_app

# Read YAML file to configure endpoints
connex_app.add_api("swagger.yaml")

config.init_db()

@app.route("/")
def home():
    """
    Returns  homepage template
    """

    return  render_template("home.html")


@app.route("/ api/bucketList")
def bucketList():
    pass

# Run if main file
if __name__ == "__main__":
    app.run(debug=True)
