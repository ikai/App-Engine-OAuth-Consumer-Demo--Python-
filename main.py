import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import oauth
from google.appengine.ext.webapp import template

# Change these values to your OAuth values
API_ENDPOINT         = "http://oauth-provider-demo.appspot.com/oauthprovider"
CONSUMER_KEY         = "consumer key"
CONSUMER_SECRET      = "consumer secret"

REQUEST_TOKEN_URL    = "http://oauth-provider-demo.appspot.com/_ah/OAuthGetRequestToken"
AUTHORIZE_TOKEN_URL  = "http://oauth-provider-demo.appspot.com/_ah/OAuthAuthorizeToken"
ACCESS_TOKEN_URL     = "http://oauth-provider-demo.appspot.com/_ah/OAuthGetAccessToken"

class MainPage(webapp.RequestHandler):
   def get(self):
      request_token = None
      
      if "request_token" in self.request.GET:
         request_token = self.request.GET["request_token"]
      
      path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
      self.response.out.write(template.render(path, {
         "request_token" : request_token
      }))
      
class GetTokenHandler(webapp.RequestHandler):
   def post(self):
      pass
      
class MakeCallHandler(webapp.RequestHandler):
   def post(self):
      pass

class CallbackHandler(webapp.RequestHandler):
   def get(self):
      pass

ROUTES = [
   ('/', MainPage),
   ('/get_token', GetTokenHandler)
]

application = webapp.WSGIApplication(ROUTES, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()