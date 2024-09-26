from flask import Flask, render_template
import socket
import os
import argparse

app = Flask(__name__)

# Get Odoo Url and PgAdmin Url from environment variables or default to None
ODOO_URL = os.environ.get('ODOO_URL', 'https://www.youtube.com/')
PGADMIN_URL = os.environ.get('PGADMIN_URL', 'https://www.youtube.com/')

@app.route("/")
def main():
    print(f'ODDO URL: {ODOO_URL}, PGADMIN URL: {PGADMIN_URL}')  # Debugging line
    return render_template('index.html', name=socket.gethostname(), odoo_url=ODOO_URL, pgadmin_url=PGADMIN_URL)

if __name__ == "__main__":
    print("This is a sample web application for intranet applications display.\n")

    # Check for Command Line Parameters for URLs
    parser = argparse.ArgumentParser()
    parser.add_argument('--odoo_url', required=False)
    parser.add_argument('--pgadmin_url', required=False)
    args = parser.parse_args()

    if args.odoo_url:
        ODOO_URL = args.odoo_url
        print("Odoo URL from command line argument =", ODOO_URL)
    else:
        print("Odoo URL from environment variable =", ODOO_URL)

    if args.pgadmin_url:
        PGADMIN_URL = args.pgadmin_url
        print("PgAdmin URL from command line argument =", PGADMIN_URL)
    else:
        print("PgAdmin URL from environment variable =", PGADMIN_URL)

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)


# from flask import Flask
# from flask import render_template
# import socket
# import random
# import os
# import argparse

# app = Flask(__name__)

# # Get Odoo Url
# ODOO_URL = os.environ.get('ODOO_URL')
# PGADMIN_URL = os.environ.get('PGADMIN_URL')

# @app.route("/")
# def main():
#     # return 'Hello'
#     return render_template('index.html', name=socket.gethostname(), odoo_url=ODOO_URL, pgadmin_url=PGADMIN_URL)

# if __name__ == "__main__":

#     print(" This is a sample web application for intranet applications display. \n"
#           "\n"
#           "")

#     # Check for Command Line Parameters for color
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--odoo_url', required=False)
#     parser.add_argument('--pgadmin_url', required=False)
#     args = parser.parse_args()

#     if args.odoo_url:
#         print("Odoo Url from command line argument =" + args.odoo_url)
#         ODOO_URL = args.odoo_url
#         if ODOO_URL:
#             print("A color was set through environment variable -" + ODOO_URL + ". However, color from command line argument takes precendence.")
#     elif ODOO_URL:
#         print("No Command line argument. Odoo url from environment variable =" + ODOO_URL)
#         ODOO_URL = ODOO_URL
#     else:
#         print("No command line argument or environment variable. Picking a Random url =")
#         ODOO_URL="https://www.youtube.com/"
  
#     if args.pgadmin_url:
#         print("Pgadmin Url from command line argument =" + args.pgadmin_url)
#         PGADMIN_URL = args.pgadmin_url
#         if PGADMIN_URL:
#             print("A color was set through environment variable -" + PGADMIN_URL + ". However, url from command line argument takes precendence.")
#     elif PGADMIN_URL:
#         print("No Command line argument. Pgadmin url from environment variable =" + PGADMIN_URL)
#         PGADMIN_URL = PGADMIN_URL
#     else:
#         print("No command line argument or environment variable. Picking a Random url =")
#         PGADMIN_URL="https://www.youtube.com/"

#     # Run Flask Application
#     app.run(host="0.0.0.0", port=8080)