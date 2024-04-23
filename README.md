Update: (23.04.2024)
A small architecture has been added to our project to select the optimal pixels without compromising the integrity of an image file.  This architecture is based on the algorithmic description of the propagation steps of a protista known in biology as Physarum polycephalum and the addition of this algorithm to Dijkstra's algorithm. These algorithms are optimization architecture designed to select the most suitable pixels for textual data to be hidden in an image.

Introduction

What is the StenoNFT?

This project is not an NFT project. The main purpose of the project is to create a chain of protocols for transforming the form of digital data and adding different data into it. The launch is based on NFTs because they are the most suitable case for the initial stage. However, our roadmap is designed with a mission to reach a technology called StenoSimulation. The logic of the algorithms and the codes provided below represent the first version of the data processing concept through NFTs.

Objectives: The main goal of StenoNFT AI is to enable images to communicate in a decentralized way by hiding and retrieving data in pixels (data packets such as classic text or program trigger codes, etc.). This system extends the use of NFTs, allowing users to develop new applications on the system. For example, data security and monitoring, automatic triggering and contract execution, tokenization and licensing, data verification and identity management, distributed transaction optimization, alternative blockchain communication module. In this way, the goal of the project is to expand the use of NFTs to perform community activities in a unique way and use NFTs more effectively in different fields.

How the StenoNFT system works? (Algorithm and Codes)

Work Phases 1 - Apply compression and encryption on the uploaded data packet

2 - Embed the representation of the compressed data packet into the pixels of the image

3 - Internet of NFT activation - APIs

STEP 1: Transforming recursive hunffman compression into an encryption protocol and creating representations

THIS step adds extra steps to the Hunffman compression algorithm, creating a 21-bit representation and keys to provide both compression and encryption.

Classic Hunffman Algorithm

In the first step, a data packet is requested from the user. For this algorithm we developed for testing purposes, the maximum number of characters in the data packet was set to 4000.

The data received from the user is compressed and bit-split by the algorithm. At this point, the algorithm creates a solution table.

Extra steps

The bit values resulting from compression are decomposed into 8s. A table is created in such a way that a new ASCII symbol is assigned to each of the 8 bits and the bits are again represented by ASCII symbols.

The classic Hunffman compression is applied again and the compressed text is compressed again. With the resulting new bits, the loop is started again and the bits are divided into 8 parts (in case the total number of bits is not exactly divided by 8, the extra bits are transferred to the first key named output. In addition to the compression process, these bits coming in each cycle help the text to shrink faster)

Repeated skimming operations continue until 7 to 21 bit representations are generated. At the end, the algorithm finishes. As output, we have an output file (key 1), a compression table (key 2) and a 7 to 21 bit ASCII value. This value is prefixed by the number of cycles during compression (this cycle information is needed to recover the text).

The process is repeated in reverse to retrieve the data packet.

In this system the anatars are delivered to the users. The 7 to 21 bit representations are both embedded in the image and stored in the blockchain. In the data retrieval process, the representation in the image is compared with the representation in the blockchain, confirmation is obtained and the reversal process starts.

Encryption also takes place through this algorithm. The ASCII combinations resulting from each compression process can be converted into a password value based on a value assigned to the user. From the last two digits of the value randomly assigned to the user, the first and last values of the number of cycles corresponding to that value can be used as a password.

Below we have created a preview running as a c# console application so you can test the algorithm

    using System;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.IO;
    namespace bitzipver1
    {
    class zipclass
    {
 

    private static string encodedText;
    static Dictionary<string, char> symbolDictionary;
    public string BitString { get; private set; }
    private static string input;
    private static string bit7input;
    private static string sozlukinput;


    
    public static string hunffmanrun(string input)
    {
        Dictionary<char, int> frequencies = CalculateFrequencies(input);
        HuffmanNode huffmanTree = BuildHuffmanTree(frequencies);
        Dictionary<char, string> huffmanCodes = GenerateHuffmanCodes(huffmanTree);
        string encodedText = EncodeText(input, huffmanCodes);

        string filepath = @"C:\Enter the path to save the table";
        zipclass zip = new zipclass();
        zip.SaveHuffmanTable(huffmanCodes, filepath);

        //string decodedText = DecodeText(encodedText, huffmanTree);
        //Console.WriteLine("Çözülmüş hali:");
        //Console.WriteLine(decodedText);


        //SaveEncodedText(encodedText, "encodedText.bin");



        // Bit sayacı
        string bits = encodedText;
        zipclass zipClass = new zipclass();  
        zipClass.ProcessBits(bits);  
        Console.WriteLine(bits);


        
        CreateSymbolDictionary();
        string bits2 = bits;
        string yenismbol = ConvertBitsToSymbols(bits2);
        Console.ForegroundColor = ConsoleColor.Green;


        Console.WriteLine(yenismbol);

        return yenismbol;
    }
  




    public static void tersineloop(string deinput, int loopCount, string abc, string cde)
    {
        ConvertSembolToSozluk(); 



        string bitler = "";

        for (int i = 0, ix = loopCount; i < loopCount && ix >= 1; i++, ix--)
        {
            string decodeInput = deinput;
            string bitlers = ConvertSembollerToBitler(decodeInput);  


            bitler = bitlers;

        


            string[] satirlar = File.ReadAllLines(cde);
            Array.Reverse(satirlar);  

            string satir = satirlar[i];

            if (satir.EndsWith("-"))
            {
                Console.WriteLine("Satırda '-' karakteri bulundu. İşlem atlandı.");
                bitler += "";
            }

            bitler += satir;  





            string bits = bitler;





            string tableFilePath = abc;  
            Dictionary<string, Dictionary<string, string>> dictionary = new Dictionary<string, Dictionary<string, string>>();

            LoadHuffmanTable(tableFilePath, dictionary);

            string groupName = "TextGroup" + ix.ToString();
            Dictionary<string, string> TextGroup = dictionary[groupName];
            dictionary.Clear();

        
            dictionary["TextGroup" + (ix + 1).ToString()] = TextGroup;

        
            Console.WriteLine("Döngü {0} için text group: {1}", ix, groupName);
            string cozulmusbits = "";

            while (!string.IsNullOrEmpty(bits))
            {
                bool sembolBulundu = false;

                foreach (KeyValuePair<string, string> kvp in TextGroup)
                {
                    string sembol = kvp.Key;
                    string bitDegeri = kvp.Value;

                    if (bits.StartsWith(bitDegeri))
                    {
           
                        bits = bits.Substring(bitDegeri.Length);

                       
                        cozulmusbits += sembol;
                        sembolBulundu = true;
                        break;
                    }

                }

                if (!sembolBulundu)
                {
                    Console.WriteLine("Hata: bir terslik var.");
                    break;
                }

            }


            Console.WriteLine("Tüm sembollerin çözülmüş bitleri:" + cozulmusbits);






            deinput = cozulmusbits; 
             

            if (i == loopCount - 1) 
            {
                string dosyaYolu = @"C:\ Enter the path ";  
                using (StreamWriter sw = new StreamWriter(dosyaYolu))
                {
                    sw.WriteLine(cozulmusbits);  
                }
            }

        }

    }




    //HUNFMAN  
    static Dictionary<char, int> CalculateFrequencies(string text)
    {
        Dictionary<char, int> frequencies = new Dictionary<char, int>();
        foreach (char c in text)
        {
            if (frequencies.ContainsKey(c))
                frequencies[c]++;
            else
                frequencies[c] = 1;
        }
        return frequencies;
    }
    static HuffmanNode BuildHuffmanTree(Dictionary<char, int> frequencies)
    {
        PriorityQueue<HuffmanNode, int> priorityQueue = new PriorityQueue<HuffmanNode, int>();
        foreach (var pair in frequencies)
        {
            priorityQueue.Enqueue(new HuffmanNode { Symbol = pair.Key, Frequency = pair.Value }, pair.Value);
        }

        while (priorityQueue.Count > 1)
        {
            HuffmanNode leftChild = priorityQueue.Dequeue();
            HuffmanNode rightChild = priorityQueue.Dequeue();

            HuffmanNode parentNode = new HuffmanNode
            {
                Symbol = '\0',
                Frequency = leftChild.Frequency + rightChild.Frequency,
                Left = leftChild,
                Right = rightChild
            };

            priorityQueue.Enqueue(parentNode, parentNode.Frequency);
        }

        return priorityQueue.Dequeue();
    }
    static void GenerateHuffmanCodesRecursive(HuffmanNode node, string code, Dictionary<char, string> codes)
    {
        if (node.Left == null && node.Right == null)
        {
            codes[node.Symbol] = code;
            return;
        }

        GenerateHuffmanCodesRecursive(node.Left, code + "0", codes);
        GenerateHuffmanCodesRecursive(node.Right, code + "1", codes);
    }
    static Dictionary<char, string> GenerateHuffmanCodes(HuffmanNode rootNode)
    {
        Dictionary<char, string> codes = new Dictionary<char, string>();
        GenerateHuffmanCodesRecursive(rootNode, "", codes);
        return codes;
    }
    static string EncodeText(string text, Dictionary<char, string> codes)
    {
        StringBuilder encodedText = new StringBuilder();
        foreach (char c in text)
        {
            encodedText.Append(codes[c]);
        }
        return encodedText.ToString();
    }
    static string DecodeText(string bits, Dictionary<string, string> huffmanCodes)
    {
        string decodedText = "";
        string currentBit = "";

        foreach (char bit in bits)
        {
            currentBit += bit;

            // Huffman kodlaması sözlüğünde eşleşme varsa sembole dönüştür
            foreach (KeyValuePair<string, string> kvp in huffmanCodes)
            {
                if (kvp.Value == currentBit)
                {
                    decodedText += kvp.Key;
                    currentBit = ""; // Bitleri sıfırla
                    break;
                }
            }
        }

        return decodedText;
    }




    // Tabloyu dosyaya kaydet

    static int textGroupCounter = 1; // Counter for text groups

    void SaveHuffmanTable(Dictionary<char, string> huffmanCodes, string filePath)
    {

        using (StreamWriter writer = new StreamWriter(filePath, true))
        {
            writer.WriteLine("TextGroup" + textGroupCounter); // Add the text group with counter
            textGroupCounter++; // Increment the counter for the next text group
            foreach (var kvp in huffmanCodes)
            {
                writer.WriteLine(kvp.Key + "π" + kvp.Value);

            }

        }
    }

    static void LoadHuffmanTable(string filePath, Dictionary<string, Dictionary<string, string>> dictionary)
    {
        string[] lines = File.ReadAllLines(filePath);
        string currentGroup = string.Empty;

        foreach (string line in lines)
        {
            if (line.StartsWith("TextGroup"))
            {
                currentGroup = line.Trim();
                dictionary[currentGroup] = new Dictionary<string, string>();

            }
            else if (!string.IsNullOrWhiteSpace(line))
            {
                string[] parts = line.Split('π');
                string key = parts[0].Trim();
                string value = parts[1].Trim();
                dictionary[currentGroup][key] = value;
            }

        }
    }






    public static void SaveEncodedText(string encodedText, string filePath)
    {
        File.WriteAllText(filePath, encodedText);
    }

    public static string LoadEncodedText(string filePath)
    {
        return File.ReadAllText(filePath);
    }

    public class HuffmanNode
    {
        public char Symbol { get; set; }
        public int Frequency { get; set; }
        public HuffmanNode Left { get; set; }
        public HuffmanNode Right { get; set; }
    }

    public static List<string> ListTextGroups(string filePath)
    {
        List<string> textGroups = new List<string>();

        if (File.Exists(filePath))
        {
            using (StreamReader reader = new StreamReader(filePath))
            {
                string line;
                StringBuilder textGroup = new StringBuilder();
                while ((line = reader.ReadLine()) != null)
                {
                    if (!string.IsNullOrWhiteSpace(line))
                    {
                        textGroup.AppendLine(line);
                    }
                    else if (textGroup.Length > 0)
                    {
                        textGroups.Add(textGroup.ToString().Trim());
                        textGroup.Clear();
                    }
                }

                // Check if there is any remaining text group
                if (textGroup.Length > 0)
                {
                    textGroups.Add(textGroup.ToString().Trim());
                }
            }
        }
        else
        {
            Console.WriteLine("Dosya bulunamadı: " + filePath);
        }

        return textGroups;
    }


    public void ProcessBits(string bits)
    {
        string outputPath = @"C:\ Enter the path output.txt";

        using (StreamWriter writer = new StreamWriter(outputPath, append: true))
        {
            int bitCount = 0; // Bit sayacı
            string output = ""; // Çıktı metni
            string bit2 = ""; // bit2 değişkeni

            for (int i = 0; i < bits.Length; i++)
            {
                output += bits[i];
                bit2 += bits[i];
                bitCount++;

                if (bitCount == 7)
                {
                    if (bitCount >= 1 && bitCount <= 6)
                    {
                        writer.WriteLine(output); // 7 bitin altındaki değerleri output.txt'ye yazdır
                    }
                    output = "";
                    bitCount = 0;
                }
            }

            if (bitCount >= 1 && bitCount <= 6)
            {
                writer.WriteLine(output); // 7 bitin altındaki değerleri output.txt'ye yazdır
            }
            else if (output == "")
            {
                writer.WriteLine("-"); // Boş döngüler için '2'yi output.txt'ye yazdır
            }


            int similarity = GetSimilarity(output, bit2); // Benzerlik oranını hesapla

            if (similarity > 0)
            {
                output = output.Substring(0, output.Length - similarity); // Benzer karakterleri sondan sil
                bit2 = bit2.Substring(0, bit2.Length - similarity); // Bit2'yi güncelle


            }
        }
    }

    private int GetSimilarity(string str1, string str2)
    {
        int similarity = 0;
        int length = Math.Min(str1.Length, str2.Length);

        for (int i = 1; i <= length; i++)
        {
            if (str1[^i] == str2[^i])
            {
                similarity++;
            }
            else
            {
                break;
            }
        }

        return similarity;
    }



    //bits2'yi (yani sayaçtan geçen inputu) ascıı yapma     
    static string ConvertBitsToSymbols(string bits2)
    {
        string yenisembol = string.Empty;
        int startIndex = 0;

        while (startIndex < bits2.Length)
        {
            int symbolLength = Math.Min(7, bits2.Length - startIndex);
            string currentSymbol = bits2.Substring(startIndex, symbolLength);

            if (symbolDictionary.ContainsKey(currentSymbol))
            {
                char symbol = symbolDictionary[currentSymbol];

                yenisembol += symbol;
            }
            else
            {
                // Geçersiz sembol, hata durumu veya özel işleme geçilebilir
                yenisembol += "";

            }

            startIndex += symbolLength;
        }

        return yenisembol;


    }

    //sözlük
    static void CreateSymbolDictionary()
    {
        symbolDictionary = new Dictionary<string, char>
    {
        { "0000000", 'Σ' },
        { "0000001", '!' },
        { "0000010", '"' },
        { "0000011", '#' },
        { "0000100", '$' },
        { "0000101", '%' },
        { "0000110", '&' },
        { "0000111", '\'' },
        { "0001000", '(' },
        { "0001001", ')' },
        { "0001010", '*' },
        { "0001011", '+' },
        { "0001100", ',' },
        { "0001101", '-' },
        { "0001110", '.' },
        { "0001111", '/' },
        { "0010000", '0' },
        { "0010001", '1' },
        { "0010010", '2' },
        { "0010011", '3' },
        { "0010100", '4' },
        { "0010101", '5' },
        { "0010110", '6' },
        { "0010111", '7' },
        { "0011000", '8' },
        { "0011001", '9' },
        { "0011010", ':' },
        { "0011011", ';' },
        { "0011100", '<' },
        { "0011101", '=' },
        { "0011110", '>' },
        { "0011111", '?' },
        { "0100000", '@' },
        { "0100001", 'A' },
        { "0100010", 'B' },
        { "0100011", 'C' },
        { "0100100", 'D' },
        { "0100101", 'E' },
        { "0100110", 'F' },
        { "0100111", 'G' },
        { "0101000", 'H' },
        { "0101001", 'I' },
        { "0101010", 'J' },
        { "0101011", 'K' },
        { "0101100", 'L' },
        { "0101101", 'M' },
        { "0101110", 'N' },
        { "0101111", 'O' },
        { "0110000", 'P' },
        { "0110001", 'Q' },
        { "0110010", 'R' },
        { "0110011", 'S' },
        { "0110100", 'T' },
        { "0110101", 'U' },
        { "0110110", 'V' },
        { "0110111", 'W' },
        { "0111000", 'X' },
        { "0111001", 'Y' },
        { "0111010", 'Z' },
        { "0111011", '[' },
        { "0111100", '\\' },
        { "0111101", ']' },
        { "0111110", '^' },
        { "0111111", '_' },
        { "1000000", '`' },
        { "1000001", 'a' },
        { "1000010", 'b' },
        { "1000011", 'c' },
        { "1000100", 'd' },
        { "1000101", 'e' },
        { "1000110", 'f' },
        { "1000111", 'g' },
        { "1001000", 'h' },
        { "1001001", 'i' },
        { "1001010", 'j' },
        { "1001011", 'k' },
        { "1001100", 'l' },
        { "1001101", 'm' },
        { "1001110", 'n' },
        { "1001111", 'o' },
        { "1010000", 'p' },
        { "1010001", 'q' },
        { "1010010", 'r' },
        { "1010011", 's' },
        { "1010100", 't' },
        { "1010101", 'u' },
        { "1010110", 'v' },
        { "1010111", 'w' },
        { "1011000", 'x' },
        { "1011001", 'y' },
        { "1011010", 'z' },
        { "1011011", '{' },
        { "1011100", '|' },
        { "1011101", '}' },
        { "1011110", '~' },
        { "1011111", 'Ç' },
        { "1100000", 'ü' },
        { "1100001", 'é' },
        { "1100010", 'â' },
        { "1100011", 'ä' },
        { "1100100", 'à' },
        { "1100101", 'å' },
        { "1100110", 'ç' },
        { "1100111", 'ê' },
        { "1101000", 'ë' },
        { "1101001", 'è' },
        { "1101010", 'ï' },
        { "1101011", 'î' },
        { "1101100", 'ì' },
        { "1101101", 'Ä' },
        { "1101110", 'Å' },
        { "1101111", 'É' },
        { "1110000", 'æ' },
        { "1110001", 'Æ' },
        { "1110010", 'ô' },
        { "1110011", 'ö' },
        { "1110100", 'ò' },
        { "1110101", 'û' },
        { "1110110", 'ù' },
        { "1110111", 'ÿ' },
        { "1111000", 'Ö' },
        { "1111001", 'Ü' },
        { "1111010", 'ø' },
        { "1111011", '£' },
        { "1111100", 'Ø' },
        { "1111101", '×' },
        { "1111110", 'ƒ' },
        { "1111111", 'á' }
        };


    }



    // VERİYİ GERİ DÖNÜŞTÜRME

    //DecodeSözlük
    static Dictionary<char, string> sembolSozlugu; // Sembol sözlüğünün ismini sembolSozlugu olarak değiştirdik

    static void ConvertSembolToSozluk()
    {
        sembolSozlugu = new Dictionary<char, string>
{

        { 'Σ', "0000000" },
        { '!', "0000001" },
        { '"', "0000010" },
        { '#', "0000011" },
        { '$', "0000100" },
        { '%', "0000101" },
        { '&', "0000110" },
        { '\'', "0000111" },
        { '(', "0001000" },
        { ')', "0001001" },
        { '*', "0001010" },
        { '+', "0001011" },
        { ',', "0001100" },
        { '-', "0001101" },
        { '.', "0001110" },
        { '/', "0001111" },
        { '0', "0010000" },
        { '1', "0010001" },
        { '2', "0010010" },
        { '3', "0010011" },
        { '4', "0010100" },
        { '5', "0010101" },
        { '6', "0010110" },
        { '7', "0010111" },
        { '8', "0011000" },
        { '9', "0011001" },
        { ':', "0011010" },
        { ';', "0011011" },
        { '<', "0011100" },
        { '=', "0011101" },
        { '>', "0011110" },
        { '?', "0011111" },
        { '@', "0100000" },
        { 'A', "0100001" },
        { 'B', "0100010" },
        { 'C', "0100011" },
        { 'D', "0100100" },
        { 'E', "0100101" },
        { 'F', "0100110" },
        { 'G', "0100111" },
        { 'H', "0101000" },
        { 'I', "0101001" },
        { 'J', "0101010" },
        { 'K', "0101011" },
        { 'L', "0101100" },
        { 'M', "0101101" },
        { 'N', "0101110" },
        { 'O', "0101111" },
        { 'P', "0110000" },
        { 'Q', "0110001" },
        { 'R', "0110010" },
        { 'S', "0110011" },
        { 'T', "0110100" },
        { 'U', "0110101" },
        { 'V', "0110110" },
        { 'W', "0110111" },
        { 'X', "0111000" },
        { 'Y', "0111001" },
        { 'Z', "0111010" },
        { '[', "0111011" },
        { '\\', "0111100" },
        { ']', "0111101" },
        { '^', "0111110" },
        { '_', "0111111" },
        { '`', "1000000" },
        { 'a', "1000001" },
        { 'b', "1000010" },
        { 'c', "1000011" },
        { 'd', "1000100" },
        { 'e', "1000101" },
        { 'f', "1000110" },
        { 'g', "1000111" },
        { 'h', "1001000" },
        { 'i', "1001001" },
        { 'j', "1001010" },
        { 'k', "1001011" },
        { 'l', "1001100" },
        { 'm', "1001101" },
        { 'n', "1001110" },
        { 'o', "1001111" },
        { 'p', "1010000" },
        { 'q', "1010001" },
        { 'r', "1010010" },
        { 's', "1010011" },
        { 't', "1010100" },
        { 'u', "1010101" },
        { 'v', "1010110" },
        { 'w', "1010111" },
        { 'x', "1011000" },
        { 'y', "1011001" },
        { 'z', "1011010" },
        { '{', "1011011" },
        { '|', "1011100" },
        { '}', "1011101" },
        { '~', "1011110" },
        { 'Ç', "1011111" },
        { 'ü', "1100000" },
        { 'é', "1100001" },
        { 'â', "1100010" },
        { 'ä', "1100011" },
        { 'à', "1100100" },
        { 'å', "1100101" },
        { 'ç', "1100110" },
        { 'ê', "1100111" },
        { 'ë', "1101000" },
        { 'è', "1101001" },
        { 'ï', "1101010" },
        { 'î', "1101011" },
        { 'ì', "1101100" },
        { 'Ä', "1101101" },
        { 'Å', "1101110" },
        { 'É', "1101111" },
        { 'æ', "1110000" },
        { 'Æ', "1110001" },
        { 'ô', "1110010" },
        { 'ö', "1110011" },
        { 'ò', "1110100" },
        { 'û', "1110101" },
        { 'ù', "1110110" },
        { 'ÿ', "1110111" },
        { 'Ö', "1111000" },
        { 'Ü', "1111001" },
        { 'ø', "1111010" },
        { '£', "1111011" },
        { 'Ø', "1111100" },
        { '×', "1111101" },
        { 'ƒ', "1111110" },
        { 'á', "1111111" }
    };





    }


    static string ConvertSembollerToBitler(string decodeInput)
    {
        StringBuilder bitler = new StringBuilder();

        foreach (char sembol in decodeInput)
        {
            if (sembolSozlugu.ContainsKey(sembol))
            {
                string bit = sembolSozlugu[sembol];
                bitler.Append(bit);
            }
            else
            {
                // Geçersiz sembol, hata durumu veya özel işleme için yapılacaklar
                // bitler.Append("");
            }
        }

        return bitler.ToString();
    }

    static string ConvertBitlerToSemboller(string bitler)
    {
        StringBuilder semboller = new StringBuilder();

        // Bitleri sembollere dönüştür
        for (int i = 0; i < bitler.Length; i += 7)
        {
            string bit = bitler.Substring(i, 7);
            char sembol = FindSembolByBit(bit);
            semboller.Append(sembol);
        }

        return semboller.ToString();
    }

    static char FindSembolByBit(string bit)
    {
        foreach (var kvp in sembolSozlugu)
        {
            if (kvp.Value == bit)
            {
                return kvp.Key;
            }
        }

        // Geçersiz bit, hata durumu veya özel işleme için yapılacaklar
        return ' ';
    }


    //dış girdi alma
    static void AppendInputToBitler(string filePath, int loopCount, ref string bitler)
    {
        string[] lines = File.ReadAllLines(filePath);
        int lineIndex = 0;

        for (int i = 0; i < loopCount; i++)
        {
            if (lineIndex >= lines.Length)
                break;

            string line = lines[lineIndex];

            if (line.Contains("-"))
            {
                lineIndex++; // Satırda "-" varsa bir sonraki satıra geç
                continue;
            }

            bitler += line;
            lineIndex++;
        }
    }



}
}

STEP 2: When the keys obtained from this compression process are delivered to the users, the 8 to 21 bit ASCII representations and the number of cycles are embedded into the image with the following stenography method.

This process maps the numeric RGB values of an image to the numeric equivalents of the ASCII symbols, embedding the data into the image. Below is a very simple shorthand algorithm that we quickly wrote in c# to demonstrate our idea.

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

After the completion of the processes, metadata containing representations are sent to the blockchain, and the reversal process also occurs through blockchain confirmation via a smart contract. Once the data sent to the blockchain is recorded, the addition of the image to the Internet of NFT network takes place.

INTERNET OF NFT NETWORK

This network is created for developers who want to develop for NFT communities. It is a feature that allows direct import of short trigger codes or long information packets into NFTs, enabling these data to dynamically communicate and perform certain operations as a result of this communication.

How does it work? At the point where a network connection is built between NFT collections for Internet of NFT, there is an infrastructure that allows the initiation or updating of the steps of a protocol for the values hidden within NFTs. These triggering processes occur with trigger codes embedded in images or in information packets containing those values.

For example, consider a scenario where a developer builds a smart contract that only includes certain collection members. At this point, the created smart contract can access the necessary transaction information by opening the information packets within the images and initiate the steps of the relevant parameters based on these parameters. This network connection allows members of a collection to use their NFTs for functions such as identification, authentication, or approval card within the collection. As the number of developers in the system increases, the areas of use will also develop in parallel.

INTETERNET OF NFT ARCHITECTURE
The Internet of NFT is a network structure in which textual data embedded in images that are minted as NFT can communicate with each other. The way this network structure works is as follows:


Textual Data Embedding Phase: First, a shorthand algorithm will be used to generate the embedded textual data. This algorithm will secretly embed textual data into a given image by modifying its pixels or adjusting its color values. This process will ensure that the data is too small to be detected by the human eye.

Embedded text can be compressed code to reveal identity and confirmation information for a transaction, or it can be groups of text generated for more specific operations. Or textual data may be embedded directly into the pixels without any compression.

Let's continue with a scenario where the images of members of an NFT collection are assigned identities and users are allowed to vote according to their status. 

Text Decoding and Identification: In the second step, the embedded textual data will be decoded from the image and the original text will be obtained. This can take place between the NFTs of the respective users, or it can be used simultaneously for all community members. This text will contain a unique ID token for each image. This ID token will be associated with smart contracts on the blockchain. 

Smart Contract Creation and Association: In the third phase, smart contracts should be created on the blockchain based on the ID token for each image, and these contracts should be identified and associated to the users. These smart contracts will be programmed to perform certain actions based on the textual data embedded in the images.

Key Confirmation and Request Submission: In the fourth step, the keys required to perform certain actions will need to be confirmed. In a network designed for users to vote, users will have 2 keys and a compressed code to embed their identity data into their images. These keys are the confirmation prompt. The approved keys will be used to send a request to the blockchain. 

Blockchain Transaction and Smart Contract Initialization: In the fifth and final step, the blockchain will validate the incoming request and initialize the smart contract. This transaction will be recorded as a specific transaction in the blockchain and the smart contract will be allowed to perform the specified action.

This process plan provides a framework for associating embedded textual data with images and enabling their integration with smart contracts on the blockchain. This scheme can be used for trusted authentication and data integrity. Or it could be designed to synchronize the stages of a game as users play it. 

A SAMPLE USE CASE FOR THE INTERNET OF NFT - ARTIFICIAL INTELLIGENCE MODEL TRAINING

This component covers the process of collecting images for visual artificial intelligence research using internet of nft and processing the labels into pixels of the image with shorthand. Users send STENO-images to a blockchain registered storage with the url address solana to create a custom model. Each image has tags embedded in its pixels. Through a parser, the tags of all the collected private images and the image itself are converted into a dataset for processing. Thus, a systematic dataset creation phase for the artificial intelligence model is realized.



