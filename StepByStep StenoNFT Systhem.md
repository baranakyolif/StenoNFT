# StenoNFT
Multilayer NFT Place Encoder/Decoder - Hunffman Loop  

Objectives:  The main goal of StenoNFT AI is to enable images to communicate in a decentralized way by hiding and retrieving data in pixels (data packets such as classic text or program trigger codes, etc.). This system extends the use of NFTs, allowing users to develop new applications on the system. For example, data security and monitoring, automatic triggering and contract execution, tokenization and licensing, data verification and identity management, distributed transaction optimization, alternative blockchain communication module. In this way, the goal of the project is to expand the use of NFTs to perform community activities in a unique way and use NFTs more effectively in different fields.


Definitions:
Sten


How the StenoNFT system works? (Algorithm and Codes)

By matching the numeric RGB values of an image with the numeric equivalents of ASCII symbols, the data is embedded into the image. Below is a version of the algorithm written in C#.

  
        using System.Drawing.Imaging;
        namespace WinFormsApp1
        {
           public partial class Form1 : Form
        {
        public Form1()
        {
            InitializeComponent();
        }
        
         
         //IMAGE UPLOAD
 
        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog openDialog = new OpenFileDialog();
            openDialog.Filter = "Image Files (*.png, *.jpg) | *.png; *.jpg";
            openDialog.InitialDirectory = @"C:\Users\metech\Desktop";

            if (openDialog.ShowDialog() == DialogResult.OK)
            {
                string originalFilePath = openDialog.FileName;

                if (Path.GetExtension(originalFilePath).Equals(".png", StringComparison.OrdinalIgnoreCase))
                {
                    pictureBox1.ImageLocation = originalFilePath;
                    textBoxFilePath.Text = originalFilePath;
                }
                else
                {
                    string pngFilePath = Path.ChangeExtension(originalFilePath, "png"); // Resmi PNG formatına dönüştürmek için yeni dosya yolunu oluşturun

                    // Resmi PNG formatına dönüştürme işlemi
                    using (Image image = Image.FromFile(originalFilePath))
                    {
                        image.Save(pngFilePath, ImageFormat.Png);
                    }

                    textBoxFilePath.Text = pngFilePath;
                    pictureBox1.ImageLocation = pngFilePath;
                }
            }
        }
        
         //STONOGRAPHY ENCODE

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap img = new Bitmap(textBoxFilePath.Text);

            for (int i = 0; i < img.Width; i++)
            {
                for (int j = 0; j < img.Height; j++)
                {
                    Color pixel = img.GetPixel(i, j);

                    if (i < 1 && j < textBoxMessage.TextLength)
                    {
                        Console.WriteLine("R = [" + i + "][" + j + "] = " + pixel.R);
                        Console.WriteLine("G = [" + i + "][" + j + "] = " + pixel.G);
                        Console.WriteLine("B = [" + i + "][" + j + "] = " + pixel.B);

                        char letter = Convert.ToChar(textBoxMessage.Text.Substring(j, 1));
                        int value = Math.Min(Math.Max(0, Convert.ToInt32(letter)), 255);
                        Console.WriteLine("letter : " + letter + " value : " + value);

                        img.SetPixel(i, j, Color.FromArgb(pixel.R, pixel.G, value));

                    }

                    if (i == img.Width - 1 && j == img.Height - 1)
                    {
                        img.SetPixel(i, j, Color.FromArgb(pixel.R, pixel.G, textBoxMessage.TextLength));
                    }
                }
            }

            //IMAGE SAVE

            SaveFileDialog saveFile = new SaveFileDialog();
            saveFile.Filter = "Image Files (*.png, *.jpg) | *.png; *.jpg";
            saveFile.InitialDirectory = @"C:\Users\metech\Desktop";

            if (saveFile.ShowDialog() == DialogResult.OK)
            {
                textBoxFilePath.Text = saveFile.FileName.ToString();
                pictureBox1.ImageLocation = textBoxFilePath.Text;

                img.Save(textBoxFilePath.Text);
            }

        }

        //STONOGRAPHY DECODE

        private void button3_Click(object sender, EventArgs e)
        {
            
            Bitmap img = new Bitmap(textBoxFilePath.Text);
            string message = "";

            Color lastpixel = img.GetPixel(img.Width - 1, img.Height - 1);
            int msgLength = lastpixel.B;

            for (int i = 0; i < img.Width; i++)
            {
                for (int j = 0; j < img.Height; j++)
                {
                    Color pixel = img.GetPixel(i, j);

                    if (i < 1 && j < msgLength)
                    {
                        int value = pixel.B;
                        char c = Convert.ToChar(value);
                        string letter = System.Text.Encoding.ASCII.GetString(new byte[] { Convert.ToByte(c) });

                        message = message + letter;
                    }
                }
            }

            richTextBox1.Text = message;
        }
    }
}


In the first stage, we used a very simple stenographic processing algorithm, where the blue color is selected in the RGB values and the values are replaced with ASCII values starting from the end. Instead of this algorithm, we could have performed stenography on the values with the lowest pixels for any color, or we could have used a password that we received from the user to select which pixels to select. However, we decided to keep this part quite simple in the first version and concentrate all our weight on repetitive hunffman combinations. In our roadmap, we aim to complicate stenographic operations in STENONFT version 1.1, which is the first update we will receive after launch.


Transforming recursive hunffman compression into an encryption protocol and creating representations









