#include <iostream>
#include <vector>

using namespace std;

/*
5 1
.X...
.X.XX
XX...
.....
.X.X.
*/

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

    struct position
    {
        int x;
        int y;
        int value;
    };

    vector<vector<position>> posibilities[n] = {};

    vector<position> temp = {};
    if (m == 1)
    {
        // Horizontal
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                cout << "\tTEMP_SIZE: " << temp.size() << endl;
                if (temp.size() + 1 == n)
                {
                    cout << "RETURNING: " << temp.size() + 1;
                    return temp.size() + 1;
                }

                if (airport[i][j] == 0)
                {
                    temp.push_back({j, i, airport[i][j]});
                }
                else
                {
                    posibilities[temp.size() - 1].push_back(temp);
                    temp.clear();
                }
            }
            posibilities[temp.size() - 1].push_back(temp);
        }

        // Vertical
        for (int i = 0; i < n; i++)
        {
            temp.clear();
            for (int j = 0; j < n; j++)
            {
                cout << "\tTEMP_SIZE: " << temp.size() << endl;
                if (temp.size() + 1 == n)
                {
                    cout << "RETURNING: " << temp.size() + 1;
                    return temp.size() + 1;
                }

                if (airport[j][i] == 0)
                {
                    temp.push_back({i, j, airport[j][i]});
                }
                else
                {
                    posibilities[temp.size() - 1].push_back(temp);
                    temp.clear();
                }
            }
            posibilities[temp.size() - 1].push_back(temp);
        }
    }
    else
    {
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
                    posibilities[temp.size() - 1].push_back(temp);
                    temp.clear();
                }
            }
            posibilities[temp.size() - 1].push_back(temp);
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