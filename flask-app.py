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

def compile_sourcecode(sourcecode, userid):
    # Compile sourcecode written in browser. Store in Redis ("bytecodes:{userid}").
    bytecodes = TestLanguage.compile_code(sourcecode)
    redis_client.set("bytecodes:{0}".format(userid), bytecodes)

    # Create the CPU. Store as serialized in Redis ("cpu:{userid}").
    cpu = Cpu(bytecodes, 512, 128, 0, 384)
    redis_client.set("cpu:{0}".format(userid), cpu.serialize_cpu())

    # Get disassembly and publish on "disassembly:{userid}" channel.
    disassembly = cpu.get_disassembly()
    redis_client.publish("disassembly:{0}".format(userid), disassembly)

    # Publish the bytecodes on the "bytecodes:{userid}" channel.
    redis_client.publish("bytecodes:{0}".format(userid), bytecodes)


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


@app.route("/compile", methods=["POST"])
def compile_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        return "Request forbidden because no userid was found.", 403

    # TODO: This can all be farmed off to a worker when they are available. Just store job in queue in Redis!!!

    sourcecode = str(request.form["sourcecode"])
    compile_sourcecode(sourcecode, userid)

    return "Ok"


@app.route("/compile-and-run", methods=["POST"])
def compile_and_run_route():
    # Check userid. If not found, abort.
    userid = request.cookies.get("userid")
    if not userid:
        return "Request forbidden because no userid was found.", 403

    # TODO: This can all be farmed off to a worker when they are available. Just store job in queue in Redis!!!

    sourcecode = str(request.form["sourcecode"])
    compile_sourcecode(sourcecode, userid)

    # TODO: Send a queue message to start executing cpu. In the mean time, just do it here.

    # Deserialize and get ready to execute.
    serialized_cpu = redis_client.get("cpu:{0}".format(userid))
    cpu = Cpu([], 512, 128, 0, 384)
    cpu.deserialize_cpu(serialized_cpu)

    # Execute.
    counter = 0
    try:
        while True:
            # Execute one step.
            cpu.execute_step()
            counter += 1

            # TODO: Output mem properly.
            if counter % 5 == 0:
                output = cpu.get_mem()
                redis_client.publish("mem:{0}".format(userid), output)

            # TODO: Output console properly.
            output = cpu.out_stream.getvalue()
            redis_client.publish("console:{0}".format(userid), output)

    except Exception as ex:
        print("Program ended. Crash?")
        pass

    finally:
        pass

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
