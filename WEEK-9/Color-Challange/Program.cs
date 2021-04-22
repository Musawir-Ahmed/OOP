using System;
using System.Collections;
using System.Windows.Forms;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Text;

namespace Color_Challange
{


    class Global_list
    {
        public static ArrayList Color_repository = new ArrayList();
    }


    class Colors
    {


        virtual public void get_colors(TextBox temp)
        {
            temp.BackColor = Color.White;
        }

        virtual public int next_color(int counter)
        {
            counter = counter + 1;
            return counter;
        }


        virtual public int prevous_color(int counter)
        {
            counter = counter - 1;
            return counter;
        }


    }

    class First_color : Colors
    {

        override public int prevous_color(int counter)
        {
            counter = Global_list.Color_repository.Count - 2;
            return counter;
        }

    }


    class Last_color : Colors
    {

        override public int next_color(int counter)
        {
            counter = 1;

            return counter;
        }
    }

    class Green : Colors
    {
        override public void get_colors(TextBox temp)
        {
            temp.BackColor = Color.Green;
        }
    }

    class Yellow : Colors
    {
        override public void get_colors(TextBox temp)
        {
            temp.BackColor = Color.Yellow;
        }
    }


    class Blue : Colors
    {
        override public void get_colors(TextBox temp)
        {
            temp.BackColor = Color.Blue;
        }
    }



    class Screen : Form
    {
        int counter = 1;
        TextBox Text_box;
        Button Next, Prevous;
        public Screen()
        {
            screen_settings();
            text_box();
            button();
        }
        void screen_settings()
        {
            this.Size = new Size(800, 500);
            this.Text = "COLO-CHANGING";
            this.CenterToScreen();
        }


        void text_box()
        {
            Text_box = new TextBox();
            Text_box.Location = new Point(50, 130);
            Text_box.Size = new Size(650, 100);
            Text_box.Text = "COLOR CHANGE";
            Text_box.Font = new Font("Calibri", 11);
            Text_box.ForeColor = Color.Black;
            this.Controls.Add(Text_box);
        }


        void button()
        {
            Next = new Button();
            Next.Location = new Point(500, 400);
            Next.Size = new Size(100, 30);
            Next.ForeColor = Color.Black;
            Next.Text = "NEXT";
            Next.BackColor = Color.RoyalBlue;
            Next.Click += new EventHandler(Next_button_click);
            this.Controls.Add(Next);


            Prevous = new Button();
            Prevous.Location = new Point(200, 400);
            Prevous.Size = new Size(100, 30);
            Prevous.ForeColor = Color.Black;
            Prevous.Text = "PREVOUS";
            Prevous.BackColor = Color.RoyalBlue;
            Prevous.Click += new EventHandler(Prevous_button_click);
            this.Controls.Add(Prevous);
        }

        private void Next_button_click(object sender, EventArgs e)
        {
            Colors color_object = (Colors)Global_list.Color_repository[counter];
            color_object.get_colors(Text_box);
            counter = color_object.next_color(counter);
        }

        private void Prevous_button_click(object sender, EventArgs e)
        {
            Colors color_object = (Colors)Global_list.Color_repository[counter];
            color_object.get_colors(Text_box);
            counter = color_object.prevous_color(counter);
        }


    }

    class Program
    {
        static void Main(string[] args)
        {
            Colors C1 = new Colors();
            First_color F1 = new First_color();
            C1 = F1;
            Global_list.Color_repository.Add(C1);

            //
            Colors C2 = new Colors();
            Green G1 = new Green();
            C2 = G1;
            Global_list.Color_repository.Add(C2);
            //
            Colors C3 = new Colors();
            Yellow Y1 = new Yellow();
            C3 = Y1;
            Global_list.Color_repository.Add(C3);
            //
            Colors C4 = new Colors();
            Blue B1 = new Blue();
            C4 = B1;
            Global_list.Color_repository.Add(C4);
            //
            Colors C5 = new Colors();
            Last_color L1 = new Last_color();
            C5 = L1;
            Global_list.Color_repository.Add(C5);

            Screen screen_object = new Screen();
            Application.EnableVisualStyles();
            Application.Run(screen_object);
        }
    }
}
