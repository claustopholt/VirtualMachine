import threading
import atexit
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import worker_monitor
import redis
import time


def generate_userid():
    # A new user is any user that doesn't have a "userid" cookie.
    userid = redis_client.incr("unique_users_count")

    # TODO: Log!
    return str(userid)


if __name__ == "__main__":

    # Start worker monitor thread.
    monitor_thread = threading.Thread(target=worker_monitor.start_monitor, args=())
    monitor_thread.start()

    # Create a redis connection.
    redis_client = redis.StrictRedis(host="128.199.43.95", port=6379, db=0)

    # Create Flask app.
    app = Flask(__name__)

    # Front page.
    @app.route("/")
    def frontpage():
        # Render response from template.
        resp = make_response(render_template("frontpage.html"))

        # Check for userid cookie.
        userid_cookie = request.cookies.get("userid")
        if not userid_cookie:
            userid = generate_userid()
            resp.set_cookie("userid", userid)

        # Render frontpage.
        return resp

    # Test route with template.
    @app.route("/blah/")
    @app.route("/blah/<name>")
    def blah(name=None):
        template = render_template("blah_template.html", name=name)
        return template

    # Test route with redis publish.
    @app.route("/test")
    def test():
        redis_client.publish("mychannel", "Test {0}".format(time.time()))
        return "Ok"

    # Run Flask app.
    app.run(debug=True, use_reloader=False)

