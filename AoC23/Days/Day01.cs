using System.Linq.Expressions;
using System.Text.RegularExpressions;

namespace AoC23.Days
{
    class Day01
    {
        public static int Part01()
        {
            List<String> input = new List<String>();
            List<int> ints = new List<int>();
            List<int> lineInts;

            string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_01.txt";

            foreach (String line in File.ReadAllLines(inputPath))
            {
                input.Add(line);
            }

            foreach (String s in input)
            {
                lineInts = new List<int>();

                for (int i = 0; i < s.Length; i++)
                {
                    if (char.IsDigit(s[i]))
                    {
                        lineInts.Add(int.Parse(s[i].ToString()));
                    }
                }

                ints.Add(int.Parse(lineInts[0].ToString() + lineInts[lineInts.Count - 1].ToString()));
            }

            Console.WriteLine(Environment.CurrentDirectory);

            return ints.Sum();
        }

        public static int Part02()
        {
            List<String> input = new List<String>();
            List<int> ints = new List<int>();
            List<int> lineInts;

            string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_01.txt";

            foreach (String line in File.ReadAllLines(inputPath))
            {
                input.Add(line);
            }

            foreach (String s in input)
            {
                lineInts = new List<int>();

                String sLine = convertLine(s);

                for (int i = 0; i < sLine.Length; i++)
                {
                    if (char.IsDigit(sLine[i]))
                    {
                        lineInts.Add(int.Parse(sLine[i].ToString()));
                    }
                }

                ints.Add(int.Parse(lineInts[0].ToString() + lineInts[lineInts.Count - 1].ToString()));
            }

            return ints.Sum();
        }

        private static string convertLine(String line)
        {
            line = line.Replace("zero", "z0o");
            line = line.Replace("one", "o1e");
            line = line.Replace("two", "t2o");
            line = line.Replace("three", "t3e");
            line = line.Replace("four", "f4r");
            line = line.Replace("five", "f5e");
            line = line.Replace("six", "s6x");
            line = line.Replace("seven", "s7n");
            line = line.Replace("eight", "e8t");
            line = line.Replace("nine", "n9e");

            return line;
        }
    }
}