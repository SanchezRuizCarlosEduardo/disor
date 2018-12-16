import TextoPlano
import Alfabeto

class Cifrador():
		
	def cifrarTipoCesar(texto, desp):
		alfabeto="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ";
		alfa = Alfabeto();
		textoCifrado = "";
		letra = "";
		posicion=0;
		for x in texto:
			print(textoCifrado);
			if alfa.buscar(x):
				posicion = alfa.buscarPosicionDeLetra(x);
				posicion = posicion + desp;
				if posicion > len(alfabeto):
					posicion = posicion - len(alfabeto);
					
				textoCifrado = textoCifrado + alfabeto[posicion];
			
			else:
				textoCifrado = textoCifrado + x;

		return textoCifrado;


	def cifrarTipoTransposicionInversa(texto):
		text = TextoPlano();
		return text.invertirTexto(texto);


	def cifrarTipoTransposicionInversaGrupos(texto,desplazamiento):
		text = TextoPlano();
		return text.invertirEnGrupos(texto,desplazamiento);