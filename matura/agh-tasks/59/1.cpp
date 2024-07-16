#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <array>

using namespace std;

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

int mocLiczby(int number)
{
    int moc = 0;

    string s = to_string(number);

    array<int, 9> arr = {};

    for (int i = 0; i < s.size(); i++)
    {
        arr[i] = s[i] - '0';
    }

    if (s.size() == 1)
    {
        return 0;
    }

    int result = arr[0];
    for (int i = 1; i < s.size(); i++)
    {
        result *= arr[i];
    }

    return mocLiczby(result) + 1;
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

    int max = numbers[0];
    int min = numbers[0];
    for (int i = 0; i < 1000; i++)
    {
        if (mocLiczby(numbers[i]) == 1)
        {
            if (numbers[i] > max)
            {
                max = numbers[i];
            }
            else if (numbers[i] < min)
            {
                min = numbers[i];
            }
        }
    }
    cout << "Result3\nmin: " << min << endl
         << "max: " << max << endl;

    return 0;
}
