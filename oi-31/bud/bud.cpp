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

int main()
{
    int n, m;
    cin >> n >> m;
    int airport[n][n];

    char area;
    for (int i = 0; i < n; i++)
    {
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

    cout << "---- END OF INPUT ----\n";

    vector<vector<position>> posibilities[n] = {};

    vector<position> temp = {};
    if (m == 1)
    {
        cout << "---- M == 1 ----\n";

        int longest = 0;

        // Horizontal
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                // if (temp.size() == n)
                // {
                //     cout << "1RETURNING: " << temp.size();
                //     return temp.size();
                // }

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
                // if (temp.size() == n)
                // {
                //     cout << "2RETURNING: " << temp.size();
                //     return temp.size();
                // }

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

        cout << "RETURNING: longest = " << longest;
        return longest;
    }
    else
    {
        cout << "---- M != 1 ----\n";

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

    cout << "\n---- POSIBILITIES ----\n";
    for (int i = 0; i < n; i++)
    {
        cout << "Size: " << i + 1 << endl;
        for (int j = 0; j < posibilities[i].size(); j++)
        {
            cout << "\tPosibility: " << j << endl;
            for (int k = 0; k < posibilities[i][j].size(); k++)
            {
                cout << "\t" << posibilities[i][j][k].x << " " << posibilities[i][j][k].y << " " << posibilities[i][j][k].value << endl;
            }
        }
    }

    for (int i = n - 1; i >= 0; i--)
    {
        if (posibilities[i].size() > 1)
        {
            cout << "i: " << i + 1 << ", posibilities[i].size(): " << posibilities[i].size() << endl;

            std::cout << (check_no_common_points(posibilities[i]) ? "True" : "False") << std::endl;

            if (check_no_common_points(posibilities[i]))
            {
                cout << "RETURNING: " << i + 1;
                return i + 1;
            }
        }
    }

    cout << "\n---- AIRPORT ----\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << airport[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}