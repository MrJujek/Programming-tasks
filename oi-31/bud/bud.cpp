#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
5 2
X....
.X.XX
X....
.X...
.X.X.
*/

struct position
{
    int x;
    int y;
    int value;
};

bool operator==(const position &a, const position &b)
{
    return a.x == b.x && a.y == b.y;
}

bool check_no_common_points(std::vector<std::vector<position>> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        for (int j = i + 1; j < arr.size(); j++)
        {
            bool common_points = false;
            for (auto &point1 : arr[i])
            {
                if (std::find(arr[j].begin(), arr[j].end(), point1) != arr[j].end())
                {
                    common_points = true;
                    break;
                }
            }
            if (!common_points)
            {
                return true;
            }
        }
    }
    return false;
}

int bud(int n, int m, int **airport)
{
    vector<vector<position>> posibilities[n] = {};

    vector<position> temp = {};
    if (m == 1)
    {
        int longest = 0;

        // Horizontal
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                if (airport[i][j] == 0)
                {
                    temp.push_back({j, i, airport[i][j]});
                }
                else
                {
                    if (temp.size() > longest)
                    {
                        longest = temp.size();
                    }
                    temp.clear();
                }
            }

            if (temp.size() > longest)
            {
                longest = temp.size();
            }
        }

        // Vertical
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                if (airport[j][i] == 0)
                {
                    temp.push_back({i, j, airport[j][i]});
                }
                else
                {
                    if (temp.size() > longest)
                    {
                        longest = temp.size();
                    }
                    temp.clear();
                }
            }

            if (temp.size() > longest)
            {
                longest = temp.size();
            }
        }

        return longest;
    }
    else
    {
        // Horizontal
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                if (airport[i][j] == 0)
                {
                    temp.push_back({j, i, airport[i][j]});
                }
                else if (temp.size() > 0)
                {
                    posibilities[temp.size() - 1].push_back(temp);
                    temp.clear();
                }
            }
            if (temp.size() > 0)
            {
                posibilities[temp.size() - 1].push_back(temp);
            }
        }

        // Vertical
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                if (airport[j][i] == 0)
                {
                    temp.push_back({i, j, airport[j][i]});
                }
                else if (temp.size() > 0)
                {
                    posibilities[temp.size() - 1].push_back(temp);
                    temp.clear();
                }
            }
            if (temp.size() > 0)
            {
                posibilities[temp.size() - 1].push_back(temp);
            }
        }
    }
    
    for (int i = n - 1; i >= 0; i--)
    {
        if (posibilities[i].size() > 1)
        {
            if (check_no_common_points(posibilities[i]))
            {
                return i + 1;
            }
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    int *airport[n];

    char area;
    for (int i = 0; i < n; i++)
    {
        airport[i] = new int[n];
        for (int j = 0; j < n; j++)
        {
            cin >> area;
            if (area == '.')
            {
                airport[i][j] = 0;
            }
            else
            {
                airport[i][j] = 1;
            }
        }
    }

    cout << bud(n, m, airport);

    return 0;
}