#!/usr/bin/env python
from urllib import urlopen
from re import search,IGNORECASE
from email.MIMEText import MIMEText
from subprocess import Popen, PIPE
from os import getenv as ge

HEADER = """
  <!doctype html>
  <html lang="en">
  <head>
  <meta charset="utf-8">
  <style>
    table {border-collapse: collapse;}
    table, td, th { border: 1px solid black;}
    td {padding-left: 4px;padding-right: 4px;}
  </style>
  </head>
  <body>
  """
FOOTER = """
  </body>
  </html>
  """

if __name__ == "__main__":
 vars = [ge('_WSURL', '-1'), ge('_SUBJECT', '-1'), ge('_EMAIL', '-1')]
 if '-1' not in vars:
  pattern = '<table align=\"CENTER\" width=\"99%\">((\n.*)*(</table>))'
  response = urlopen(vars[0]).read() #returns an entire page
  result = search(pattern, response, IGNORECASE).group(0) # grab only data from response
  context = HEADER + result + FOOTER
  msg = MIMEText(context,'html')
  msg["To"] = vars[2]
  msg["Subject"] = vars[1]
  p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
  p.communicate(msg.as_string())
