from nagare import component, presentation


class Transposicion(object):

    def __init__(self):
        self.val = 0
        #Alfabeto
        #MensajeTextoPlano
        #MensajeCifrado


@presentation.render_for(Transposicion)
def render(counter, h, *args):
    h << h.h1('Cifrado por transposicion')
    h << h.h3('Ingrese grupo:')
    h << h.input(type="number")
    h << h.h3('texto cifrado:')
    h << h.textarea(cols=40, rows=4)



    return h.root
# ---------------------------------------------------------------

app = Transposicion