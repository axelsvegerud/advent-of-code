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

        public static String Part02()
        {
            return "Part 2";
        }
    }
}