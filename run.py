from __future__ import unicode_literals, absolute_import, print_function

import webapp2

from holidays import views

application = webapp2.WSGIApplication([
    ('/', views.MainPage),
    ('/calendar/', views.Calendar),
], debug=False)
