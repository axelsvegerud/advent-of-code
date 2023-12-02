namespace AoC23.Days
{
    class Day02
    {
        static string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_02.txt";
        static int redMax = 12;
        static int greenMax = 13;
        static int blueMax = 14;

        public static int Part01()
        {
            List<string> input = new List<string>();

            foreach (string line in File.ReadAllLines(inputPath))
            {
                input.Add(line);
            }

            List<string> possibleGames = getPossibleGames(input, redMax, greenMax, blueMax);
            List<int> IDs = getIDs(possibleGames);

            return IDs.Sum();
        }

        private static List<string> getPossibleGames(List<string> list, int redLimit, int greenLimit, int blueLimit)
        {
            List<string> possibleGames = new List<string>();
            bool possible;

            foreach (string line in list)
            {
                possible = true;
                string trimedLine = line.Substring(line.IndexOf(':') + 1);
                string[] sets = trimedLine.Split(';');
                foreach (string set in sets)
                {
                    string[] colors = set.Split(",");
                    foreach (string color in colors)
                    {
                        if (color.Contains("red"))
                        {
                            if (int.Parse(string.Concat(color.Where(char.IsDigit).ToArray())) > redLimit)
                            {
                                possible = false;
                            }
                        }
                        else if (color.Contains("green"))
                        {
                            if (int.Parse(string.Concat(color.Where(char.IsDigit).ToArray())) > greenLimit)
                            {
                                possible = false;
                            }
                        }
                        else if (color.Contains("blue"))
                        {
                            if (int.Parse(string.Concat(color.Where(char.IsDigit).ToArray())) > blueLimit)
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

        private static List<int> getIDs(List<string> list)
        {
            List<int> IDs = new List<int>();

            foreach (string line in list)
            {
                if (line[6].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 1)));
                }
                else if (line[7].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 2)));
                }
                else if (line[8].Equals(':'))
                {
                    IDs.Add(int.Parse(line.Substring(5, 3)));
                }
            }

            return IDs;
        }

        public static int Part02()
        {
            List<string> input = new List<string>();

            foreach (string line in File.ReadAllLines(inputPath))
            {
                input.Add(line);
            }

            List<string[]> fewestNbrCubes = getFewestCubes(input);
            List<int> powerSets = getPower(fewestNbrCubes);

            return powerSets.Sum();
        }

        private static List<string[]> getFewestCubes(List<string> games)
        {
            List<string[]> fewest = new List<string[]>();

            foreach (string line in games)
            {
                int red = 0;
                int green = 0;
                int blue = 0;

                string trimedLine = line.Substring(line.IndexOf(':'));
                string[] sets = trimedLine.Split(';');
                foreach (string set in sets)
                {
                    string[] colors = set.Split(',');
                    foreach (string color in colors)
                    {
                        if (color.Contains("red"))
                        {
                            int currentRed = int.Parse(string.Concat(color.Where(char.IsDigit).ToArray()));
                            if (currentRed > red)
                            {
                                red = currentRed;
                            }
                        }
                        else if (color.Contains("green"))
                        {
                            int currentGreen = int.Parse(string.Concat(color.Where(char.IsDigit).ToArray()));
                            if (currentGreen > green)
                            {
                                green = currentGreen;
                            }
                        }
                        else if (color.Contains("blue"))
                        {
                            int currentBlue = int.Parse(string.Concat(color.Where(char.IsDigit).ToArray()));
                            if (currentBlue > blue)
                            {
                                blue = currentBlue;
                            }
                        }
                    }
                }
                fewest.Add([$"Red: {red}", $"Green: {green}", $"Blue: {blue}"]);
            }
            return fewest;
        }

        private static List<int> getPower(List<string[]> list)
        {
            List<int> power = new List<int>();
            foreach (string[] s in list)
            {
                int redVal = int.Parse(string.Concat(s[0].Where(char.IsDigit).ToArray()));
                int greenVal = int.Parse(string.Concat(s[1].Where(char.IsDigit).ToArray()));
                int blueVal = int.Parse(string.Concat(s[2].Where(char.IsDigit).ToArray()));

                power.Add(redVal * greenVal * blueVal);
            }
            return power;
        }
    }
}