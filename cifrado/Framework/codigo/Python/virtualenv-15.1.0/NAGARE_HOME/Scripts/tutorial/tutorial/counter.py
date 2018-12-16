from nagare import presentation


class Counter(object):

    def __init__(self):
        self.val = 0
        #Alfabeto
        #MensajeTextoPlano
        #MensajeCifrado


    def increase(self):
        self.val += 1

    def decrease(self):
        self.val -= 1


@presentation.render_for(Counter)
def render(counter, h, *args):
    h << h.div('Value: ', counter.val)

    h << h.a('++').action(counter.increase)
    h << '|'
    h << h.a('--').action(counter.decrease)

    return h.root

@presentation.render_for(Counter, model='freezed')
def render(counter, h, *args):
    return h.h1(counter.val)

# ---------------------------------------------------------------

app = Counter
