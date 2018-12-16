from nagare import component, presentation

class Cesar(object):

    def __init__(self):
        self.val = 0
        #Alfabeto
        #MensajeTextoPlano
        #MensajeCifrado


@presentation.render_for(Cesar)
def render(counter, h, *args):
    h << h.h1('Cifrado Cesar')
    h << h.h3('Ingrese desplazamiento:')  
    h << h.input(type="number")
    h << h.h3('texto cifrado:')
    h << h.textarea(cols=40, rows=4)



    return h.root
# ---------------------------------------------------------------

app = Cesar
