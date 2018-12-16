

namespace CifradoCesarCshare
{
    class Cifrador
    {
        Alfabeto alfabeto;
        TextoPlano textoPlano;

        public Cifrador(Alfabeto abecedario)
        {
            alfabeto = abecedario;
        }

        public string CifradoTipoCesar(string texto, int desplazamiento)
        {
            textoPlano = new TextoPlano(texto);
            string textoCifrado = "";
            int posicion = 0;

            for (int i = 0; i < textoPlano.textoPlano.Length; i++)
            {
                if (alfabeto.perteneceAlfabeto(textoPlano.textoPlano[i]))
                {
                    posicion = alfabeto.buscarPosicionLetra(textoPlano.textoPlano[i]);
                    posicion = posicion + desplazamiento;

                    if (posicion > alfabeto.caracteres.Length)
                        posicion = posicion - alfabeto.caracteres.Length;

                    textoCifrado = textoCifrado + alfabeto.caracteres[posicion];
                }
                else
                    textoCifrado = textoCifrado + textoPlano.textoPlano[i];
            }

            return textoCifrado;
        }

        public string cifradoTipoTransposicionInversa(string texto)
        {
            textoPlano = new TextoPlano(texto);
            return textoPlano.invertirTexto();
        }


        public string cifradoTipoTransposicionInversaPorGrupos(string texto,int desplazamiento)
        {
            textoPlano = new TextoPlano(texto);
            return textoPlano.invertirTextoGrupos(desplazamiento);
        }

       
        
    }
}
