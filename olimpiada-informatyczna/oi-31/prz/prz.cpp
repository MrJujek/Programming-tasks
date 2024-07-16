#include <iostream>
#include <algorithm>

int main()
{
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    int i, j;

    int n, m;
    int button_id = 1;

    std::cin >> n >> m;

    if (m < n || m > n * n)
    {
        std::cout << "NIE\n";
        return 0;
    }

    int buttons_board[n][n];
    std::fill(&buttons_board[0][0], &buttons_board[0][0] + n * n, 0);
    int buttons_list[m][2];

    int a, b;
    for (i = 0; i < m; i++)
    {
        std::cin >> a >> b;
        buttons_board[a - 1][b - 1] = button_id++;

        buttons_list[i][0] = a - 1;
        buttons_list[i][1] = b - 1;
    }

    // for (i = 0; i < m; i++)
    // {

    // }

    std::cout << "--- buttons_list ---\n";
    for (i = 0; i < m; i++)
    {
        std::cout << buttons_list[i][0] + 1 << " " << buttons_list[i][1] + 1 << std::endl;
    }

    if (m == n * n)
    {
        std::cout << "TAK\n";
        for (i = 0; i < m; i++)
        {
            std::cout << buttons_list[i][0] + 1 << " " << buttons_list[i][1] + 1 << std::endl;
        }
        return 0;
    }

    std::cout << "--- buttons_board ---\n";
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            std::cout << buttons_board[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
