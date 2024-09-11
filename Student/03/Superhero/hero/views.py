from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Nergigante',
            'body': 'Monster Type: Elder Dragon',
            'image': '/static/images/nergigante.jpg'
        }


class IronManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Espinas',
            'body': 'Monster Type: Flying Wyverns',
            'image': '/static/images/espinas.jpg'
        }


class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Bazelgeuse',
            'body': 'Monster Type: Flying Wyverns',
            'image': '/static/images/bazelgeuse.jpg'
        }
