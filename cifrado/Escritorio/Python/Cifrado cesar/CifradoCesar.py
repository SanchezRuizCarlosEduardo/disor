from gi.repository import Gtk

alfabeto="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ";
def buscarPosicionDeLetra(letra):
		posicion=-1;
		p = 0;

		parar = 0;
		while parar<len(alfabeto):
			if letra==alfabeto[parar]:
				posicion=parar;

			parar=parar+1;


		return posicion;


def  buscar(letra):
	encontre = False;
	parar = 0;
	while parar<len(alfabeto):
		if letra==alfabeto[parar]:
			encontre=True;

		parar=parar+1;

	return encontre;


def cifrar(texto, desp):
	textoCifrado = "";
	letra = "";
	posicion=0;
	for x in texto:
		print(textoCifrado);
		if buscar(x):
			posicion = buscarPosicionDeLetra(x);
			posicion = posicion + desp;
			if posicion > len(alfabeto):
				posicion = posicion - len(alfabeto);
				
			textoCifrado = textoCifrado + alfabeto[posicion];
		
		else:
			textoCifrado = textoCifrado + x;

	return textoCifrado;



def invertirTexto(texto):
	textoInvertido = "";
	stop = len(texto)-1;

	while stop>=0:
		textoInvertido=textoInvertido+texto[stop];
		stop = stop -1;

	return textoInvertido;

def invertirEnGrupos(texto, grupos):
	textoInvertido="";
	textito="";
	tam=0;
	pos=0;
	stop=0;

	while len(texto)>stop:
		if (stop % grupos) == 0:
			textoInvertido = textoInvertido + invertirTexto(textito);
			textito = texto[stop];
		else:
			textito=textito+texto[stop];

		stop = stop+1;

	return textoInvertido+textito;





def cifrartxt(entry):
    txtPlano = builder.get_object("entry1")
    txtDespl = builder.get_object("entry5");
    txtTamG = builder.get_object("entry6");
    txtCifrado = builder.get_object("entry2");
    txtInverso = builder.get_object("entry3");
    txtInversoG = builder.get_object("entry4");

    txtAcifrar = txtPlano.get_text()
    desp = int(txtDespl.get_text())
    tamG = int(txtTamG.get_text())


    textoCifrado = cifrar(txtAcifrar, desp)
    textoInverso = invertirTexto(txtAcifrar)
    textoInversoG =invertirEnGrupos(txtAcifrar, tamG)

    txtCifrado.set_text(textoCifrado)
    txtInverso.set_text(textoInverso)
    txtInversoG.set_text(textoInversoG)

    
    
    
    

builder = Gtk.Builder()
builder.add_from_file("InterfazGrafica.glade")
handlers = {
    "terminar_app": Gtk.main_quit,
    "cifrarTexto": cifrartxt
}

builder.connect_signals(handlers)
window = builder.get_object("ventana_principal")
window.show_all()

Gtk.main()
