#include <iostream>
#include <vector>

void assign_codes(int n, int p, int M, const std::vector<std::pair<int, int>> &connections)
{
    char codes[] = {'A', 'B', 'C'};

    // Inicjalizacja kodów identyfikacyjnych
    std::vector<std::string> satellite_codes(2 * n + 1, "");

    // Przydzielanie kodów dla par satelitów
    for (int i = 1; i <= n; ++i)
    {
        satellite_codes[i] = {codes[0]};
        satellite_codes[i] += codes[1];
        satellite_codes[i] += codes[2];

        satellite_codes[i + n] = {codes[1]};
        satellite_codes[i + n] += codes[0];
        satellite_codes[i + n] += codes[2];

        std::swap(codes[0], codes[1]);
        std::swap(codes[1], codes[2]);
    }

    // Ustawianie komunikacji między satelitami tej samej firmy
    for (int i = 1; i <= n; ++i)
    {
        for (int j = i + 1; j <= n; ++j)
        {
            satellite_codes[j][1] = satellite_codes[i][1];
            satellite_codes[j + n][1] = satellite_codes[i + n][1];
        }
    }

    // Ustawianie komunikacji między satelitami różnych firm
    for (const auto &connection : connections)
    {
        int a = connection.first;
        int b = connection.second;
        satellite_codes[b] = satellite_codes[a];
    }

    // Wypisanie wyniku
    std::cout << M << std::endl;
    for (int i = 1; i <= 2 * n; ++i)
    {
        std::cout << satellite_codes[i] << std::endl;
    }
}

int main()
{
    int n, p, M;
    std::cin >> n >> p >> M;

    std::vector<std::pair<int, int>> connections;
    for (int i = 0; i < p; ++i)
    {
        int a, b;
        std::cin >> a >> b;
        connections.push_back({a, b});
    }

    assign_codes(n, p, M, connections);

    return 0;
}