import threading
import atexit
from flask import Flask
from flask import render_template
import worker_monitor


if __name__ == "__main__":

    # Start worker monitor thread.
    monitor_thread = threading.Thread(target=worker_monitor.start_monitor, args=())
    monitor_thread.start()

    # Create Flask app.
    app = Flask(__name__)

    # Front page.
    @app.route("/")
    def frontpage():
        template = render_template("frontpage.html")
        return template

    # Test route with template.
    @app.route("/blah/")
    @app.route("/blah/<name>")
    def blah(name=None):
        template = render_template("blah_template.html", name=name)
        return template

    # Run Flask app.
    app.run(debug=True, use_reloader=False)

