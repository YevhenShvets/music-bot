using Npgsql;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FilmMusicAdmin
{
    class DB
    {
        public static string strConnString = "Server=localhost;Port=5432;Username=music_user;Password=music_telebot_password;Database=f_test";
        public static NpgsqlConnection objConn;

        public static void getInstance()
        {
            if (objConn==null)
            {
                objConn = new NpgsqlConnection(strConnString);
            }
        }


        public static void insert_film(string name, string type, string description, string director, byte[] photo)
        {
            try
            {
                objConn.Open();
                string strSelectCmd = "INSERT INTO \"Film\"(name, type, description, director, image_url) VALUES(@name, @type, @description, @director, @image_url)";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@name", name);
                cmd.Parameters.AddWithValue("@type", type);
                cmd.Parameters.AddWithValue("@description", description);
                cmd.Parameters.AddWithValue("@director", director);
                cmd.Parameters.AddWithValue("@image_url", photo);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Додано", "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
        }

        public static void insert_music(string name, string author, byte[] music)
        {
            try
            {
                objConn.Open();
                string strSelectCmd = "INSERT INTO \"Music\"(name, author, url) VALUES(@name, @author, @url)";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@name", name);
                cmd.Parameters.AddWithValue("@author", author);
                cmd.Parameters.AddWithValue("@url", music);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Додано", "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
        }

        public static void insert_music_film(int film_id, int music_id)
        {
            try
            {
                objConn.Open();
                string strSelectCmd = "INSERT INTO \"Film_Music\"(film_id, music_id) VALUES(@fid, @mid)";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@fid", film_id);
                cmd.Parameters.AddWithValue("@mid", music_id);
                cmd.ExecuteNonQuery();
                //MessageBox.Show("Добавлено", "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
        }

        public static int select_music_id(string name, string author)
        {
            int result = -1;
            try
            {
                objConn.Open();
                string strSelectCmd = "SELECT id FROM \"Music\" WHERE name=@name AND author=@author;";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@name", name);
                cmd.Parameters.AddWithValue("@author", author);
                NpgsqlDataReader dataReader = cmd.ExecuteReader();
                while (dataReader.Read())
                {
                    result = Convert.ToInt32(dataReader[0]);
                    break;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
            return result;
        }

        public static List<string> select_films()
        {
            List<string> result = new List<string>();
            try
            {
                objConn.Open();
                string strSelectCmd = "SELECT id, name FROM \"Film\";";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                NpgsqlDataReader dataReader =  cmd.ExecuteReader();
                while(dataReader.Read()){
                    result.Add(dataReader[0].ToString() + "_" + dataReader[1].ToString());
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
            return result;
        }

        public static List<string> select_musics()
        {
            List<string> result = new List<string>();
            try
            {
                objConn.Open();
                string strSelectCmd = "SELECT id, name FROM \"Music\";";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                NpgsqlDataReader dataReader = cmd.ExecuteReader();
                while (dataReader.Read())
                {
                    result.Add(dataReader[0].ToString() + "_" + dataReader[1].ToString());
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
            return result;
        }

        public static void deleteFilm(int film_id)
        {
            try
            {
                objConn.Open();
                string strSelectCmd = "DELETE FROM \"Film\" WHERE id=@id";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@id", film_id);

                cmd.ExecuteNonQuery();
                MessageBox.Show("Вилучено", "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
        }

        public static void deleteMusic(int music_id)
        {
            try
            {
                objConn.Open();
                string strSelectCmd = "DELETE FROM \"Music\" WHERE id=@id";
                var cmd = new NpgsqlCommand(strSelectCmd, objConn);
                cmd.Parameters.AddWithValue("@id", music_id);

                cmd.ExecuteNonQuery();
                MessageBox.Show("Вилучено", "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error message", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                objConn.Close();
            }
        }


    }
}
