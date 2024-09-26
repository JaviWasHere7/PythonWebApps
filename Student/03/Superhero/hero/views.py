from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class DeadPoolView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Deadpool',
            'body': '"With great power comes great merchandising opportunity."',
            'image': '/static/images/Deadpool.webp'
        }


class SpiderManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'body': '"Anyone can wear the mask. You could wear the mask."',
            'image': '/static/images/Spiderman.jpg'
        }


class BatmanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Batman',
            'body': '"Even After Everything You’ve Done, I Would’ve Saved You."',
            'image': '/static/images/Batman.webp'
        }
    
class IronmanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Ironman',
            'body': '“I’m sorry, Earth is closed today. You better pack it up and get outta here.”',
            'image': '/static/images/Iron_Man.webp'
        }
    
class GambitView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Gambit',
            'body': '"Woo, I’m about to make a name for myself!"',
            'image': '/static/images/Gambit.jpg'
        }