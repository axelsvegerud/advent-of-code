using System.Text;

namespace AoC23.Days
{
    class Day03
    {
        static string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_03.txt";
        //static string inputPath = $"{Environment.CurrentDirectory}\\Input\\test.txt";

        public static int Part01()
        {
            List<string> input = [.. File.ReadAllLines(inputPath)];

            List<int> nbrs = [];

            for (int i = 0; i < input.Count; i++)
            {
                for (int j = 0; j < input[i].Length; j++)
                {
                    if (Char.IsDigit(input[i][j]) && adjacentToSymbol(input, i, j))
                    {
                        StringBuilder sb = new StringBuilder();
                        nbrs.Add(getNumber(input, i, j, sb));
                    }
                }
            }
            return nbrs.Sum();
        }

        public static string Part02()
        {
            return "Part 2";
        }

        private static bool adjacentToSymbol(List<string> list, int row, int col)
        {
            for (int i = row - 1; i <= row + 1; i++)
            {
                for (int j = col - 1; j <= col + 1; j++)
                {
                    if (i >= 0 && i < list.Count && j >= 0 && j < list[i].Length)
                    {
                        if (i == row && j == col)
                        {
                            continue;
                        }
                        if (!Char.IsDigit(list[i][j]) && list[i][j] != '.')
                        {
                            return true;
                        }
                    }
                }
            }
            return false;
        }

        private static int getNumber(List<string> list, int row, int col, StringBuilder sb)
        {
            while (col != 0)
            {
                if (Char.IsDigit(list[row][col - 1]))
                {
                    col = col - 1;
                }
                else
                {
                    break;
                }
            }

            sb.Append(list[row][col]);

            while (col < list[row].Length - 1)
            {
                if (Char.IsDigit(list[row][col + 1]))
                {
                    col = col + 1;
                    sb.Append(list[row][col]);
                    list[row] = list[row].Substring(0, col) + ' ' + list[row].Substring(col + 1);
                }
                else
                {
                    break;
                }
            }

            return int.Parse(sb.ToString());
        }

        static void ExtendNumberSequence(string[] lines, int row, int col, StringBuilder sequence)
        {
            for (int i = row - 1; i <= row + 1; i++)
            {
                for (int j = col - 1; j <= col + 1; j++)
                {
                    if (i == row && j == col)
                        continue;

                    if (i >= 0 && i < lines.Length && j >= 0 && j < lines[i].Length)
                    {
                        char adjacentChar = lines[i][j];

                        if (Char.IsDigit(adjacentChar))
                        {
                            sequence.Append(adjacentChar);
                            // Mark the digit as visited to avoid duplicate counting
                            lines[i] = lines[i].Substring(0, j) + ' ' + lines[i].Substring(j + 1);
                            ExtendNumberSequence(lines, i, j, sequence);
                        }
                    }
                }
            }
        }
    }
}
