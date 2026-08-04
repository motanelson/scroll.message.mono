using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace helloworld
{
    
    public partial class Form1 : Form
    {
        private int i = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            i = label1.Left + label1.Width;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Left = label1.Left - 10;
            if (label1.Left < -label1.Width - 10) label1.Left = i;
        }
    }
}
