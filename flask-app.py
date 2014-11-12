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
    # Render response from template.
    resp = make_response(render_template("frontpage.html"))

    # Check for userid cookie.
    userid_cookie = request.cookies.get("userid")
    if not userid_cookie:
        userid = generate_userid()
        resp.set_cookie("userid", userid)

    # Render frontpage.
    return resp


@app.route("/compile", methods=["GET", "POST"])
def compile_sourcecode():
    # Check userid. If not found, abort.
    userid_cookie = request.cookies.get("userid")
    if not userid_cookie:
        return "Request forbidden because no userid was found.", 403

    # TODO: This can all be farmed off to a worker when they are available. Just store job in queue in Redis!!!

    # Compile sourcecode written in browser. Store in Redis ("bytecodes:{userid}").
    sourcecode = str(request.form["sourcecode"])
    bytecodes = TestLanguage.compile_code(sourcecode)
    redis_client.set("bytecodes:{0}".format(userid_cookie), bytecodes)

    # Create the CPU. Store as serialized in Redis ("cpu:{userid}").
    cpu = Cpu(bytecodes, 512, 128, 0, 384)
    redis_client.set("cpu:{0}".format(userid_cookie), cpu.serialize_cpu())

    # Get disassembly and publish on "disassembly:{userid}" channel.
    disassembly = cpu.get_disassembly()
    redis_client.publish("disassembly:{0}".format(userid_cookie), disassembly)

    # Publish the bytecodes on the "bytecodes:{userid}" channel.
    redis_client.publish("bytecodes:{0}".format(userid_cookie), bytecodes)

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
