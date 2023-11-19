#include <array>
#include <iostream>
#include <vector>
#include <fstream>
// #include <filesystem>
#include <string>

struct testcase
{
    long long n;
    long long k;
    long long a;
    long long b;
    std::string S;
};

std::string ChatBBB(long long k, long long a, long long b, std::string S)
{
    long long n = S.size();

    if (n == b)
        return S.substr(a - 1, b);

    std::string suffix = S.substr(n - k, n);

    long long pos = 0;
    std::array<long long, 128> arr;
    arr.fill(0);

    char most_common = 'a';
    while (S.find(suffix, pos) != std::string::npos)
    {
        long long _pos = S.find(suffix, pos);
        char c = S[_pos + k];
        arr[c]++;

        if (arr[c] > arr[most_common])
        {
            most_common = c;
        }
        else if (arr[c] == arr[most_common])
        {
            if (c < most_common)
            {
                most_common = c;
            }
        }

        pos = _pos + 1;
    }

    S += most_common;
    return ChatBBB(k, a, b, S);
}

int main()
{
    struct errors
    {
        int test_id;
        std::string expected;
        std::string actual;
    };

    std::vector<errors>
        error_list = {};

    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    long long N, k, a, b;
    std::string S;

    int test_id;
    // std::cin >> test_id;
    // for (int i = test_id * 1000 - 1000 + 1; i <= test_id * 1000; i++)
    for (int i = 3000 + 1; i <= 4000; i++)
    {
        std::cout << "Test ID: " << i << std::endl;

        std::fstream input;
        input.open("../../oi_2023_testy/cza/in/" + std::to_string(i) + ".in", std::ios::in);

        std::fstream output;
        output.open("../../oi_2023_testy/cza/out/" + std::to_string(i) + ".out", std::ios::in);

        if (!input.is_open() || !output.is_open())
        {
            i++;
            std::cout << "File not found: " << i << std::endl;
            continue;
        }

        input >> N >> k >> a >> b >> S;

        // std::cout << "N: " << N << std::endl;
        // std::cout << "k: " << k << std::endl;
        // std::cout << "a: " << a << std::endl;
        // std::cout << "b: " << b << std::endl;
        // std::cout << "S: " << S << std::endl;

        std::string expected;
        output >> expected;

        // std::cout << "Expected: " << expected << std::endl;

        std::string actual = ChatBBB(k, a, b, S);

        // std::cout << "Actual: " << actual << std::endl;

        if (expected != actual)
        {
            error_list.push_back({i, expected, actual});
        }

        input.close();
        output.close();
    }

    if (error_list.size() == 0)
    {
        std::cout << "OK" << std::endl;
    }
    else
    {
        std::cout << "Errors: " << std::endl;
        for (auto &error : error_list)
        {
            std::cout << "Test ID: " << error.test_id << std::endl;
            std::cout << "Expected: " << error.expected << std::endl;
            std::cout << "Actual: " << error.actual << std::endl
                      << std::endl;
        }

        std::cout << "Errors number: " << error_list.size() << std::endl;
    }

    // std::cin >> N >> k >> a >> b >> S;

    // std::cout << ChatBBB(k, a, b, S) << std::endl;

    return 0;
}