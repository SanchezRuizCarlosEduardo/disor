class Alfabeto

	def buscarPosicionDeLetra(letra)
			alfabeto="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"
			posicion=-1
			p = 0
			parar = 0
			while parar<alfabeto.length-1
				if letra==alfabeto[parar]
					posicion=parar
				end
				parar=parar+1
			end
		return posicion
	end
	

	def  buscar(letra)
		alfabeto="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"
		encontre = false
		parar = 0;
		while parar<alfabeto.length
			if letra==alfabeto[parar]
				encontre=true;
			end
			
			parar=parar+1;
		end
		return encontre;
	end