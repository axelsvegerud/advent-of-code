using System.Diagnostics;

namespace AoC23.Days
{
    class Day04
    {
        static string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_04.txt";
        //static string inputPath = $"{Environment.CurrentDirectory}\\Input\\test.txt";

        public static int Part01()
        {
            List<string> input = [.. File.ReadAllLines(inputPath)];

            int totalPoints = 0;

            for (int i = 0; i < input.Count; i++)
            {
                string line = input[i].Substring(input[i].IndexOf(':') + 2);

                int[] cardNumbers = getNumbers(line.Substring(0, line.IndexOf('|') - 1));
                int[] winningNumbers = getNumbers(line.Substring(line.IndexOf('|') + 2));

                totalPoints += getPoints(cardNumbers, winningNumbers);
            }
            return totalPoints;
        }

        private static int[] getNumbers(string numbers)
        {
            var numberList = new List<int>();
            foreach (string s in numbers.Split(' '))
            {
                if(!s.Equals(""))
                {
                    numberList.Add(int.Parse(s));
                }
            }
            return numberList.ToArray();
        }

        private static int getPoints(int[] cardNumbers, int[] winningNumbers)
        {
            int points = 0;
            for (int i = 0; i < cardNumbers.Length; i++)
            {
                if (winningNumbers.Contains(cardNumbers[i]))
                {
                    if (points == 0)
                    {
                        points++;
                    }
                    else
                    {
                        points = points * 2;
                    }
                }
            }
            return points;
        }

        public static int Part02()
        {
            return 0;
        }
    }
}