#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int n = 1000;
vector<bool> isPrime(n, true);

int rozklad(int x)
{
    int i = 3;

    set<int> czynniki;

    while (x > 1)
    {
        while (x % i == 0)
        {
            x /= i;
            czynniki.insert(i);
        }
        i++;
    }

    return czynniki.size();
}

bool czyPalindrom(string s)
{
    for (int i = 0; i < s.size() / 2; i++)
    {
        if (s[i] != s[s.size() - 1 - i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    fstream file;
    file.open("liczby.txt", ios::in);

    vector<int> numbers;

    int number;
    for (int i = 0; i < 1000; i++)
    {
        file >> number;
        numbers.push_back(number);
    }

    for (int i = 0; i < 1000; i++)
    {
        cout << numbers[i] << endl;
    }

    isPrime[1] = false;
    isPrime[2] = true;

    for (int i = 2; i < n; i++)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j < n; j += i)
            {
                isPrime[j] = false;
            }
        }
    }

    cout << endl
         << isPrime[16] << endl;

    int result1 = 0;

    for (int i = 0; i < 1000; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            continue;
        }

        if (rozklad(numbers[i]) == 3)
        {
            result1++;
        }
    }

    cout << "Result 1: " << result1 << endl;

    int result2 = 0;
    for (int i = 0; i < 1000; i++)
    {
        string b1 = to_string(numbers[i]);
        string b2 = "";
        for (int j = b1.size() - 1; j >= 0; j--)
        {
            b2 += b1[j];
        }

        if (czyPalindrom(to_string(stoi(b2) + stoi(b1))))
        {
            result2++;
        }
    }

    cout << "Result 2: " << result2 << endl;

    return 0;
}
