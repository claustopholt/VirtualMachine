import threading
import time
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import worker_monitor
import redis
import TestLanguage
from cpu import Cpu


# Create Flask app.
app = Flask(__name__)


# A new user is any user that doesn't have a "userid" cookie.
def generate_userid():
    # Generate a new userid in Redis.
    userid = redis_client.incr("unique_users_count")

    # TODO: Log!
    return str(userid)

@app.route("/")
def frontpage():
    # Check for userid cookie.
    userid_cookie = request.cookies.get("userid")
    if not userid_cookie:
        userid = generate_userid()
    else:
        userid = userid_cookie

    # Get latest sourcecode from Redis ("sourcecode:{userid}").
    sourcecode = redis_client.get("sourcecode:{0}".format(userid))

    # Render response from template.
    resp = make_response(render_template("frontpage.html", sourcecode=sourcecode))

    # Set cookie if it wasn't present in the request.
    if not userid_cookie:
        resp.set_cookie("userid", userid)

    # Render frontpage.
    return resp


# TODO: Wrapper method that checks userid cookie!
@app.route("/compile", methods=["POST"])
def compile_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        return "Request forbidden because no userid was found.", 403

    # Store sourcecode then push the compile command to the redis queue "commandqueue".
    redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
    redis_client.set("sourcecode:{0}".format(userid), request.form["sourcecode"])
    redis_client.lpush("commandqueue", "compile:{0}".format(userid))
    return "Ok"


@app.route("/compile-and-run", methods=["POST"])
def compile_and_run_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        return "Request forbidden because no userid was found.", 403

    # Store sourcecode then push the compile-and-run command to the redis queue "commandqueue".
    redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
    redis_client.set("sourcecode:{0}".format(userid), request.form["sourcecode"])
    redis_client.lpush("commandqueue", "compile-and-run:{0}".format(userid))
    return "Ok"


@app.route("/test")
def test():
    # Test route with redis publish.
    redis_client.publish("mychannel", "Test {0}".format(time.time()))
    return "Ok"


if __name__ == "__main__":

    # Start worker monitor thread.
    monitor_thread = threading.Thread(target=worker_monitor.start_monitor, args=())
    monitor_thread.start()

    # Create a redis connection.
    redis_client = redis.StrictRedis(host="128.199.43.95", port=6379, db=0)

    # Run Flask app.
    app.run(debug=True, use_reloader=False)
