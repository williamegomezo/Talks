from quart import Quart
from db import Session
from blueprints import auth_blueprint, websockets_blueprint

app = Quart(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(websockets_blueprint)

@app.teardown_appcontext
async def teardown_db(resp_or_exc):
    Session.remove()

app.run()