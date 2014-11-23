from holidays import views

import webapp2

application = webapp2.WSGIApplication([
    ('/', views.MainPage),
    ('/calendar/', views.Calendar),
], debug=True)
