#!/usr/bin/env python3
#

from flask import Flask, request, redirect, url_for

from newsdb import most_popular_articles, author_rank, error_rate

app = Flask(__name__)

HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis</title>
    <style>
      h1, div.answer{ text-align: center; }
      span.articles { font-style: italic; }
      span.authors, span.date { font-weight: bold; }
    </style>
  </head>
  <body>
    <h1>Most popular three articles of all time</h1>
    %s
    <h1>Most popular article authors of all time</h1>
    %s
    <h1>Date with more than 1%% of requests lead to errors</h1>
    %s
  </body>
</html>
'''

# HTML template for an individual comment
POST1 = '''\
    <div class=answer> <span class=articles>"%s"</span> --- %s Views </div>
'''
POST2 = '''\
    <div class=answer> <span class=authors>%s</span> --- %s Views </div>
'''
POST3 = '''\
    <div class=answer> <span class=date>%s</span> --- %s%% Errors </div>
'''


@app.route('/', methods=['GET'])
def main():
    ans1 = "".join(POST1 % (title, rank)
                   for title, rank in most_popular_articles())
    ans2 = "".join(POST2 % (name, acount) for name, acount in author_rank())
    ans3 = "".join(POST3 % (date, erate) for date, erate in error_rate())
    html = HTML_WRAP % (ans1, ans2, ans3)

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
