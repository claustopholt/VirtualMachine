from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import redis
import VMLogger


# Create Flask app.
app = Flask(__name__)
VMLogger.log_info("Flask app is created.")

# Create a Redis connection.
redis_client = redis.StrictRedis(host="redis.topholt.com", port=6379, db=0)
VMLogger.log_info("Redis client is established.")


# A new user is any user that doesn't have a "userid" cookie.
def generate_userid():
    # Generate a new userid in Redis.
    userid = redis_client.incr("unique_users_count")
    VMLogger.log_info("New userid {0} is created.".format(userid))
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

    # Render response from template, incl. userid cookie if not found in request.
    resp = make_response(render_template("frontpage.html", sourcecode=sourcecode))
    if not request.cookies.get("userid"):
        resp.set_cookie("userid", userid)

    # Render frontpage.
    return resp


@app.route("/compile", methods=["POST"])
def compile_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        VMLogger.log_info("Request forbidden because no userid was found.")
        return "Request forbidden because no userid was found.", 403

    # Store sourcecode then push the compile command to the redis queue "commandqueue".
    redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
    redis_client.set("sourcecode:{0}".format(userid), request.form["sourcecode"])
    redis_client.lpush("commandqueue", "compile:{0}".format(userid))
    VMLogger.log_info("Source code received and stored in queue to be compiled.")
    return "Ok"


@app.route("/compile-and-run", methods=["POST"])
def compile_and_run_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        VMLogger.log_info("Request forbidden because no userid was found.")
        return "Request forbidden because no userid was found.", 403

    # Store sourcecode then push the compile-and-run command to the redis queue "commandqueue".
    redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
    redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
    redis_client.set("sourcecode:{0}".format(userid), request.form["sourcecode"])
    redis_client.lpush("commandqueue", "compile-and-run:{0}".format(userid))
    VMLogger.log_info("Source code received and stored in queue to be compiled and executed.")
    return "Ok"


@app.route("/examples")
def examples_route():
    return render_template("examples.html")


@app.route("/disassembly")
def disassembly_route():
    VMLogger.log_info("test disassembly")
    return render_template("disassembly.html")


@app.route("/memory")
def memory_route():
    return render_template("memory.html")


if __name__ == "__main__":
    # If not run in gunicorn, run app locally.
    VMLogger.log_info("Flask app is run locally (with debug=True).")
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
