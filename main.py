# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
  	welcome_template = the_jinja_env.get_template('templates/index.html')
  	self.response.write(welcome_template.render())

 

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ], debug=True)














