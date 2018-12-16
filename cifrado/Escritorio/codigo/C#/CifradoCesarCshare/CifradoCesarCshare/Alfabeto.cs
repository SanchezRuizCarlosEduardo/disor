using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CifradoCesarCshare
{
    class Alfabeto
    {
        public String caracteres;
        
        public Alfabeto(String letras)
        {
            caracteres = letras;
        }

        public int buscarPosicionLetra(char letra)
        {
            for (int i = 0; i < caracteres.Length; i++)
                if (caracteres[i] == letra)
                    return i;

            return -1;
        }

        public bool perteneceAlfabeto(char letra)
        {
            for (int i = 0; i < caracteres.Length; i++)
                if (caracteres[i] == letra)
                    return true;

            return false;
        }
        
    }
}
