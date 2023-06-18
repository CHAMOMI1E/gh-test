from flask import Flask
from ghost import GhostAdmin
from dotenv import dotenv_values

app = Flask(__name__)


@app.route("/")
def start():
    config = dotenv_values(".env")
    # .env can be used, but config values can also be simply hardcoded
    ga = GhostAdmin(
        config["GHOST_SITE"],
        # adminAPIKey=config["GHOST_ADMIN_KEY"],
        # contentAPIKey=config["GHOST_CONTENT_KEY"],
        api_version="v4",
    )
    print(ga.site())


if __name__ == '__main__':
    app.run()
