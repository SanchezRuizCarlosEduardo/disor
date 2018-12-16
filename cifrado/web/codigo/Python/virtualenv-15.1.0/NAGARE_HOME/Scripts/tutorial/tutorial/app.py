from nagare import component, presentation
from counter import Counter
from nagare.namespaces import xhtml


class App(object):

    def __init__(self):
        self.counter1 = component.Component(Counter(), model='freezed')
        self.counter2 = component.Component(Counter())
        self.counter1.becomes(self.counter1, model='freezed')

@presentation.render_for(App)
def render(self, h, *args):
    h << self.counter1.render(xhtml.AsyncRenderer(h))
    h << h.br
    h << self.counter2

    return h.root

	# factory
app = App