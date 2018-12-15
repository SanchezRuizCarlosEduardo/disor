using System;

namespace CifradoCesarCshare
{
    class TextoPlano
    {
        public String textoPlano;

        public TextoPlano(string texto)
        {
            textoPlano = texto;
        }

        public string invertirTexto()
        {
            string textoInvertido = "";
            for (int i = textoPlano.Length - 1; i >= 0; i--)
                textoInvertido = textoInvertido + textoPlano[i];

            return textoInvertido;
        }

        private string invertirTexto(string textito)
        {
            string textoInvertido = "";
            for (int i = textito.Length - 1; i >= 0; i--)
                textoInvertido = textoInvertido + textito[i];

            return textoInvertido;
        }

        public string invertirTextoGrupos(int grupos)
        {
            string textoInvertido = "";
            string textito = "";

            for (int i = 0; i < textoPlano.Length; i++)
            {
                if ((i) % grupos == 0)
                {
                    textoInvertido = textoInvertido + invertirTexto(textito);
                    textito = "" + textoPlano[i];
                }
                else
                    textito = textito + textoPlano[i];
            }

            return textoInvertido + textito;
        }
        
    }
}
