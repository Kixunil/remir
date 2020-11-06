from bottle import route, run
from subprocess import call
import subprocess
import time
import toml
from os import urandom

@route("/<password>")
def index(password):
    global PASSWORD
    if password != PASSWORD:
        return "Invalid password"

    result = """
    <html>
    <head>
        <title>IR remote control</title>
        <script>
        function send(btn) {
            var request = new XMLHttpRequest();
            request.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    alert(this.responseText);
                }
            };
            request.open("GET", window.location.href + "/send/" + btn, true);
            request.send();
        }
        </script>
    </head>
    <body>
    """

    for remote in subprocess.run(["irsend", "LIST", "", ""], stdout=subprocess.PIPE, check=True).stdout.decode("utf-8").split('\n'):
        if remote == "":
            continue

        for button in subprocess.run(["irsend", "LIST", remote, ""], stdout=subprocess.PIPE, check=True).stdout.decode("utf-8").split('\n'):
            if button == "":
                continue

            _, button_name = button.split(' ')
            result += """<button onclick="send('%s/%s')">%s - %s</button>""" % (remote, button_name, remote, button_name)

    result += """
    </body>
    </html>
    """

    return result

@route("/<password>/send/<remote>/<command>")
def send(password, remote, command):
    global PASSWORD
    if password != PASSWORD:
        return "Invalid password"

    if call(["irsend", "SEND_ONCE", remote, command]) != 0:
        return "Command failed"

    return "OK"

def main():
    global PASSWORD
    config = toml.load("/etc/remir/remir.toml")
    if "password" in config:
        PASSWORD = config["password"]
    else:
        PASSWORD = urandom(16).hex()

    if "bind_address" in config:
        bind_address = config["bind_address"]
    else:
        bind_address = "127.0.0.1"

    with open("/var/run/remir/password", "w", encoding="utf-8") as password_file:
        password_file.write(PASSWORD)

    run(host=bind_address, port=config["port"], debug=True)
