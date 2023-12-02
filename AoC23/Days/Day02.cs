using System.Runtime.CompilerServices;

namespace AoC23.Days
{
    class Day02
    {
        static string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_02.txt";

        public static int Part01()
        {
            int redMax = 12;
            int greenMax = 13;
            int blueMax = 14;
            List<String> input = new List<String>();

            foreach (String line in File.ReadAllLines(inputPath))
            {
                input.Add(line);
            }

            List<String> possibleGames = getPossibleGames(input, redMax, greenMax, blueMax);
            List<int> IDs = getIDs(possibleGames);

            return IDs.Sum();
        }

        private static List<String> getPossibleGames(List<String> list, int red, int green, int blue)
        {
            List<String> possibleGames = new List<String>();
            bool possible;

            foreach (String line in list)
            {
                possible = true;
                String trimedLine = line.Substring(line.IndexOf(':') + 1);
                string[] sets = trimedLine.Split(';');
                foreach (String set in sets)
                {
                    String[] colors = set.Split(",");
                    foreach (String color in colors)
                    {
                        if (color.Contains("red"))
                        {
                            if (int.Parse(string.Concat(color.Where(Char.IsDigit).ToArray())) > red)
                            {
                                possible = false;
                            } 
                        } else if (color.Contains("green"))
                        {
                            if (int.Parse(string.Concat(color.Where(Char.IsDigit).ToArray())) > green)
                            {
                                possible = false;
                            }
                        }
                        else if (color.Contains("blue"))
                        {
                            if (int.Parse(string.Concat(color.Where(Char.IsDigit).ToArray())) > blue)
                            {
                                possible = false;
                            }
                        }
                    }
                }

                if (possible)
                {
                    possibleGames.Add(line);
                }
            }

            return possibleGames;
        }

        private static List<int> getIDs(List<String> list)
        {
            List<int> IDs = new List<int>();

            foreach (String line in list)
            {
                if (line[6].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 1)));
                } else if (line[7].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 2)));
                } else if (line[8].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 3)));
                }
            }

            return IDs;
        }

        public static String Part02()
        {
            return "Part 2";
        }
    }
}