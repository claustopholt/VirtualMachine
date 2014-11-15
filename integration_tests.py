import unittest
from TinyLanguage import TinyLanguage
from antlr4 import InputStream
from VMCpu import VMCpu
import time
import flask_app
import httplib
import multiprocessing


# Note: These are more integration tests than unit tests.
class TestCpu(unittest.TestCase):

    # Helper method that starts up the Flask app.
    def helper_run_flask_app(self):
        flask_app.app.run(host="127.0.0.1", port=5001, debug=True, use_reloader=False)

    # Simple sanity check integration test.
    def test_compile_and_execute_program(self):

        # Compile program and check that bytecodes were produced.
        sourcecode = InputStream.InputStream("script { a = 10; b = 2; if (a * b == 20) { output(40 / b); } }")
        bytecodes = TinyLanguage.compile_code(sourcecode)
        self.assertTrue(len(bytecodes) > 5)

        # Execute program and check that the result is 20 in less than 50 steps.
        output = ""
        counter = 0
        try:
            cpu = VMCpu(bytecodes, 512, 128, 0, 384)
            while True:
                counter += 1
                output += cpu.execute_step()
        except:
            self.assertTrue(counter < 50)
            self.assertTrue(output == "20\r\n")
            pass

    def test_flask_app(self):
        # Spawn up the Flask app on port 5001.
        process = multiprocessing.Process(target=self.helper_run_flask_app)
        process.start()

        # Check that the front page contains the word "Virtual Machine"
        http_connection = httplib.HTTPConnection("127.0.0.1", 5001)
        http_connection.request("GET", "/")
        response = http_connection.getresponse()
        body = response.read()
        self.assertTrue("Virtual Machine" in body)

        # Check that a POST to /compile returns a 403 (because test has no userid cookie).
        http_connection.request("POST", "/compile")
        response = http_connection.getresponse()
        self.assertTrue(response.status == 403)

        # Stop the Flask app.
        process.terminate()
