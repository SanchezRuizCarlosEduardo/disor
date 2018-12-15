class Alfabeto():

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
