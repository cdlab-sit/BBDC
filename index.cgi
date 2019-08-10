#!/home/purplealpaca1/.pyenv/versions/moguenv/bin/python


import cgitb
cgitb.enable(display=0, logdir="/home/purplealpaca1/www/mogumogu/BBDC/log.txt")

from wsgiref.handlers import CGIHandler
from server import app
CGIHandler().run(app)
