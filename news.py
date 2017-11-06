from flask import Flask, request, redirect, url_for

from newsdb import get_top_authors, get_top_articles, get_fails

app = Flask(__name__)

# HTML for the landing page of our report
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Sourabh's Report</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>


    <h1>Top Articles of the archive</h1>
    <p>%s</p>
    <h1>Top Authors of our generation</h1>
     <p>%s</p>
<h1>The day of excess access failures</h1>
     <p>%s</p>
  </body>
</html>
'''



POST_ARTICLES = '''\
    <div>
    <ul>
    <li>"%s" - %s views </li>
    </ul>

    </div>
'''

POST_AUTHORS = '''\
    <div>
    <ul>
    <li>%s - %s views </li>
    </ul>

    </div>
'''



POST_FAILS = '''\
    <div>
    <ul>
    <li>%s - %s%%  errors </li>
    </ul>

    </div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts_authors = "".join(POST_AUTHORS % (name, counts) for name, counts in get_top_authors())
  posts_articles = "".join(POST_ARTICLES % (articles, counts) for articles, counts in get_top_articles())
  post_fails = "".join(POST_FAILS % (date, errors) for date, errors in get_fails())
  html = HTML_WRAP % (posts_articles, posts_authors, post_fails)
  return html





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
