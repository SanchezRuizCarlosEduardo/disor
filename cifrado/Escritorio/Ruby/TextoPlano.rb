class TextoPlano


	
	def invertirTexto(texto)
		textoInvertido = ""
		stop = texto.length-1

		while stop>=0
			textoInvertido=textoInvertido+texto[stop]
			stop = stop -1
		end
		
		return textoInvertido
	end



	def invertirEnGrupos(texto, grupos)
		textoInvertido=""
		textito=""
		tam=0
		pos=0
		stop=0

		while texto.length>stop do
			if (stop % grupos) == 0
				textoInvertido = textoInvertido + invertirTexto(textito)
				textito = texto[stop]
			else
				textito=textito+texto[stop]
			end
			stop = stop+1
		end
		return textoInvertido+textito
	end