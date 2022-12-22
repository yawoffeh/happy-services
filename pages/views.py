from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'index.html'

class SignPageView(TemplateView): 
    template_name = 'sign.html'
    
class LoginPageView(TemplateView):
	template_name = 'log.html'
