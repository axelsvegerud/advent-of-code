using System.Text;

namespace AoC23.Days
{
    class Day03
    {
        static string inputPath = $"{Environment.CurrentDirectory}\\Input\\Input_03.txt";

        public static int Part01()
        {
            List<string> input = [.. File.ReadAllLines(inputPath)];

            List<int> nbrs = [];

            for (int i = 0; i < input.Count; i++)
            {
                for (int j = 0; j < input[i].Length; j++)
                {
                    if (char.IsDigit(input[i][j]) && adjacentToSymbol(input, i, j))
                    {
                        StringBuilder sb = new StringBuilder();
                        nbrs.Add(getNumber(input, i, j, sb));
                    }
                }
            }
            return nbrs.Sum();
        }

        public static int Part02()
        {
            List<string> input = [.. File.ReadAllLines(inputPath)];

            List<int> nbrs = [];

            for (int i = 0; i < input.Count; i++)
            {
                for (int j = 0; j < input[i].Length; j++)
                {
                    if (input[i][j] == '*')
                    {
                        int[] gearRetio = getNeighbors(input, i, j);
                        if (gearRetio.Length == 2)
                        {
                            nbrs.Add(gearRetio[0] * gearRetio[1]);
                        }
                    }
                }
            }
            return nbrs.Sum();
        }

        private static int[] getNeighbors(List<string> list, int row, int col)
        {
            List<int> ratio = new List<int>();

            for (int i = -1; i <= 1; i++)
            {
                for (int j = -1; j <= 1; j++)
                {
                    if (i == 0 && j == 0)
                    {
                        continue;
                    }
                    else
                    {
                        int rowIndex = row + i;
                        int colIndex = col + j;

                        if (rowIndex >= 0 && rowIndex < list.Count && colIndex >= 0 && colIndex < list[rowIndex].Length)
                        {
                            if (char.IsDigit(list[rowIndex][colIndex]))
                            {
                                StringBuilder sb = new StringBuilder();
                                ratio.Add(getNumber(list, rowIndex, colIndex, sb));
                            }
                        }
                    }
                }
            }
            return ratio.ToArray();
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
                        if (!char.IsDigit(list[i][j]) && list[i][j] != '.')
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
                if (char.IsDigit(list[row][col - 1]))
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
                if (char.IsDigit(list[row][col + 1]))
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
    }
}
