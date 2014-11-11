import threading
import atexit
from flask import Flask
from flask import render_template
import worker_monitor


def create_app():
    # Create Flask app with a monitor thread.
    app = Flask(__name__)
    global monitor_thread

    # Allow the Flask app to close down thread.
    def interrupt():
        global monitor_thread
        monitor_thread.cancel()

    # Front page.
    @app.route("/")
    def hello():
        return "Hello World!"

    # Test route with template.
    @app.route("/blah/")
    @app.route("/blah/<name>")
    def blah(name=None):
        template = render_template("blah_template.html", name=name)
        return template

    # Register interrupt and return app.
    atexit.register(interrupt)
    return app


if __name__ == "__main__":
    # Start at worker monitor, which will spawn up workers and keep them alive.
    monitor_thread = threading.Thread(target=worker_monitor.monitor, args=())
    monitor_thread.start()

    # Create the Flask app.
    app = create_app()
    app.run(debug=True)

