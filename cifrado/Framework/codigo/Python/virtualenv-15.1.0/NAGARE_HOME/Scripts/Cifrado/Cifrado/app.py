#from __future__ import with_statement

#import os
from nagare import component, presentation
from cesar import Cesar
from transposicion import Transposicion
from transposicioninversa import TransposicionInversa

class Cifrado(object):
   
   def __init__(self):
        self.cesar1 = component.Component(Cesar())
        self.transposicion1 = component.Component(Transposicion())
        self.transposicioninversa1 = component.Component(TransposicionInversa())
        self.val = 0


   def cambiar(self):
       	self.val += 1


@presentation.render_for(Cifrado)
def render(self, h, *args):

    h.head << h.head.title('** Cifrados **')

    
    h << h.h1('Cifrados:')
    h << h.h2('Ingrese texto a cifrar: ')
                

    h << h.textarea(cols=40, rows=4)
    h << h.a('++').action(self.cambiar)
    h << h.div('Valor de val: ', self.val)
    h << h.textarea(cols=40, rows=4, value=self.val)


    h << self.cesar1
    h << h.br
    h << self.transposicion1
    h << h.br
    h << self.transposicioninversa1

    with h.div():#with h.div(id='footer'):
        with h.table:
            with h.tr:
                with h.td:
                    with h.ul:
                        h << h.h1('Cifrado por desplazamiento')
                        h << h.h3('Ingrese desplazamiento:')  
                        h << h.input(type="number")
                        h << h.h3('texto cifrado:')
                        h << h.textarea(cols=40, rows=4)
                with h.td:
                    with h.ul:
                      	h << h.h1('Cifrado por transposicion')
                        h << h.h3('Ingrese grupo:')
                        h << h.input(type="number")
                        h << h.h3('texto cifrado:')
                        h << h.textarea(cols=40, rows=4)

                with h.td(class_='last'):
                    with h.ul:
                      	h << h.h1('Cifrado por transposicion')
                        h << h.h3('texto cifrado:')
                        h << h.textarea(cols=40, rows=4)
                        h << h.br()
                        h << h.br()
                        h << h.br()
                        h << h.br()
                        h << h.br()
    return h.root


# ---------------------------------------------------------------

app = Cifrado
