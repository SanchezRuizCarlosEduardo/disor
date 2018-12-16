requiere 'Alfabeto'
requiere 'TextoPlano'

class Cifrador

	def initialize(algo)
		@iii=algo

	def cifrar(texto, desp)
		textoCifrado = ""
		letra = ""
		posicion=0
		alfabeto="aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"
		 texto.each_char do |caracter|

   			if buscar(caracter)
				posicion = buscarPosicionDeLetra(caracter)
				posicion = posicion + desp
				if posicion > alfabeto.length
					posicion = posicion - alfabeto.length
				end

				textoCifrado = textoCifrado + alfabeto[posicion]
			
			else
				textoCifrado = textoCifrado + caracter
			end

		end 


		return textoCifrado
	end



	def cifrarTipoTransposicion(texto)
		tp = TextoPlano.new()
		return tp.invertirTexto(texto)


	def cifrarTipoTransposicionGrupos(texto,desplazamiento)
		tp = TextoPlano.new()
		return tp.invertirEnGrupos(texto,desplazamiento)