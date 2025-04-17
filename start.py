import socket
import sys
import webbrowser
import threading

from src.main import app


def is_port_in_use(port):
    """Check if a port is already in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def open_browser():
    """Open the app in the user's default web browser."""
    webbrowser.open("http://localhost:5000")


if __name__ == "__main__":
    if is_port_in_use(5000):
        print("App is already running at http://localhost:5000")
        webbrowser.open("http://localhost:5000")
        sys.exit(0)

    threading.Timer(1.25, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
