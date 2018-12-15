class TextoPlano():
	
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