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
