from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import oauth

class MainPage(webapp.RequestHandler):
   def get(self):
      self.response.out.write("<html><head>")
      self.response.out.write('<meta name="google-site-verification" content="y9JU-YRZyuWXD_fCq122gvABdYljIrbezu1SXX7ox1M" />')
      self.response.out.write("</head><body>Hi</body>")
      self.response.out.write("</html>")
      
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()