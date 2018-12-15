using System;
using System.Windows.Forms;
using CifradoCesarCshare;

namespace CifradoCesarCshare
{

    public partial class InterfazGrafica : Form
    {
        Alfabeto alfabeto;
        Cifrador cifrador;

        public InterfazGrafica()
        {
            InitializeComponent();
            alfabeto = new Alfabeto("aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ");
            cifrador = new Cifrador(alfabeto);
        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            string texto = textBox1.Text;
            string desp = desplaza1.Text;
            string agrupacion = ValorAgrup.Text;


            int d = System.Convert.ToInt16(desp);
            int a = System.Convert.ToInt16(agrupacion);

            textBox2.Text = cifrador.CifradoTipoCesar(texto, d);
            textBox3.Text = cifrador.cifradoTipoTransposicionInversa(texto);
            textBox4.Text = cifrador.cifradoTipoTransposicionInversaPorGrupos(texto, a);

        }
        

    }
}

