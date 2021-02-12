using Npgsql;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FilmMusicAdmin
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string name = textBox1.Text;
            string type = textBox2.Text;
            string description = richTextBox1.Text;
            string director = textBox3.Text;

            if(name.Length>0 && type.Length>0 && description.Length>0 && director.Length>0)
                using (OpenFileDialog dlg = new OpenFileDialog())
                {
                    dlg.Title = "Завантажити фотографію";
                    dlg.Filter = "photo|*.png;*.jpg;s*.jpeg";

                    if (dlg.ShowDialog() == DialogResult.OK)
                    {
                        FileInfo fileInfo = new FileInfo(dlg.FileName);
                        byte[] data = new byte[fileInfo.Length];
                        using (FileStream fs = fileInfo.OpenRead())
                        {
                            fs.Read(data, 0, data.Length);
                        }
                        DB.insert_film(name, type, description, director, data);
                        textBox1.Text = "";
                        textBox2.Text = "";
                        richTextBox1.Text = "";
                        textBox3.Text = "";
                    }
                    else
                    {
                        MessageBox.Show("Файл не вибрано", "Помилка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            else
            {
                MessageBox.Show("Перевірте введені дані", "Помилка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            update();

        }

        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void update_data_film()
        {
            Dictionary<string, string> films = new Dictionary<string, string>();
            foreach (string val in DB.select_films())
            {
                string[] v = val.Split('_');
                films.Add(v[0], v[1]);
            }
            if (films.Count > 0)
            {
                comboBox1.DataSource = new BindingSource(films, null);
                comboBox1.DisplayMember = "Value";
                comboBox1.ValueMember = "Key";

                comboBox3.DataSource = new BindingSource(films, null);
                comboBox3.DisplayMember = "Value";
                comboBox3.ValueMember = "Key";
            }
            else
            {
                comboBox1.DataSource = null;
                comboBox3.DataSource = null;
            }
        }

        private void update_data_musics()
        {
            Dictionary<string, string> musics = new Dictionary<string, string>();
            foreach (string val in DB.select_musics())
            {
                string[] v = val.Split('_');
                musics.Add(v[0], v[1]);
            }
            if (musics.Count > 0)
            {
                comboBox2.DataSource = new BindingSource(musics, null);
                comboBox2.DisplayMember = "Value";
                comboBox2.ValueMember = "Key";
            }
            else
            {
                comboBox2.DataSource = null;
            }
        }

        private void update()
        {
            update_data_film();
            update_data_musics();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DB.getInstance();
            update();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int film_id = Convert.ToInt32(comboBox1.SelectedValue.ToString());
            DB.deleteFilm(film_id);
            update();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string film_id = comboBox3.SelectedValue.ToString();

            string name = textBox6.Text;
            string author = textBox5.Text;

            if (name.Length > 0 && author.Length > 0)
                using (OpenFileDialog dlg = new OpenFileDialog())
                {
                    dlg.Title = "Завантажити музичний трек";
                    dlg.Filter = "song|*.mp3;*.m4a;";

                    if (dlg.ShowDialog() == DialogResult.OK)
                    {
                        FileInfo fileInfo = new FileInfo( dlg.FileName);
                        byte[] data = new byte[fileInfo.Length];
                        using (FileStream fs = fileInfo.OpenRead())
                        {
                            fs.Read(data, 0, data.Length);
                        }
                        DB.insert_music(name, author, data);
                        DB.insert_music_film(Convert.ToInt32(film_id), DB.select_music_id(name, author));
                        textBox6.Text = "";
                        textBox5.Text = "";
                    }
                    else
                    {
                        MessageBox.Show("Файл не вибрано", "Помилка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            else
            {
                MessageBox.Show("Перевірте введені дані", "Помилка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            update();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int music_id = Convert.ToInt32(comboBox2.SelectedValue.ToString());
            DB.deleteMusic(music_id);
            update();
        }
    }
}
