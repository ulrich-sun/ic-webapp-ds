from flask import Flask, render_template
import socket
import os
import argparse

app = Flask(__name__)

# Get Odoo Url
ODOO_URL = os.environ.get('ODOO_URL')
PGADMIN_URL = os.environ.get('PGADMIN_URL')
missing_vars = []

@app.route("/")
def main():
    return render_template('index.html', name=socket.gethostname(), odoo_url=ODOO_URL, pgadmin_url=PGADMIN_URL)

@app.route("/env-error")
def env_error():
    return render_template('env_error.html', missing_vars=missing_vars)

if __name__ == "__main__":

    print(" This is a sample web application for intranet applications display. \n")

    # Check for Command Line Parameters for URLs
    parser = argparse.ArgumentParser()
    parser.add_argument('--odoo_url', required=False)
    parser.add_argument('--pgadmin_url', required=False)
    args = parser.parse_args()

    if args.odoo_url:
        print("Odoo Url from command line argument =" + args.odoo_url)
        ODOO_URL = args.odoo_url
    elif not ODOO_URL:
        print("No command line argument or environment variable. Redirecting to /env-error.")
        missing_vars.append('ODOO_URL')
        ODOO_URL = "/env-error"
  
    if args.pgadmin_url:
        print("Pgadmin Url from command line argument =" + args.pgadmin_url)
        PGADMIN_URL = args.pgadmin_url
    elif not PGADMIN_URL:
        print("No command line argument or environment variable. Redirecting to /env-error.")
        missing_vars.append('PGADMIN_URL')
        PGADMIN_URL = "/env-error"

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
