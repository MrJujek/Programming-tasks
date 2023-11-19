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

    std::cout << "N: " << n << std::endl;
    std::cout << "b: " << b << std::endl;

    if (n == b)
        return S.substr(a - 1, b);

    std::string suffix = S.substr(n - k, n);
    std::cout << "Suffix: " << suffix << std::endl;

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

    std::cout << "Most common: " << most_common << std::endl;

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

    // int test_id;
    // // std::cin >> test_id;
    // // for (int i = test_id * 1000 - 1000 + 1; i <= test_id * 1000; i++)
    // std::fstream input;
    // std::fstream output;

    // std::fstream errors_file;
    // errors_file.open("errors.txt", std::ios::out);

    // for (int i = 3000 + 1; i <= 4000; i++)
    // {
    //     std::cout << "Test ID: " << i << std::endl;

    //     input.open("../../oi_2023_testy/cza/in/" + std::to_string(i) + ".in", std::ios::in);

    //     output.open("../../oi_2023_testy/cza/out/" + std::to_string(i) + ".out", std::ios::in);

    //     if (!input.is_open() || !output.is_open())
    //     {
    //         i++;
    //         std::cout << "File not found: " << i << std::endl;
    //         continue;
    //     }

    //     input >> N >> k >> a >> b >> S;

    //     // std::cout << "N: " << N << std::endl;
    //     // std::cout << "k: " << k << std::endl;
    //     // std::cout << "a: " << a << std::endl;
    //     // std::cout << "b: " << b << std::endl;
    //     // std::cout << "S: " << S << std::endl;

    //     std::string expected;
    //     output >> expected;

    //     // std::cout << "Expected: " << expected << std::endl;

    //     std::string actual = ChatBBB(k, a, b, S);

    //     // std::cout << "Actual: " << actual << std::endl;

    //     if (expected != actual)
    //     {
    //         error_list.push_back({i, expected, actual});

    //         errors_file << "Test ID: " << i << std::endl;
    //         errors_file << "Expected: " << expected << std::endl;
    //         errors_file << "Actual: " << actual << std::endl
    //                     << std::endl;
    //     }

    //     input.close();
    //     output.close();
    // }

    // errors_file.close();

    // if (error_list.size() == 0)
    // {
    //     std::cout << "OK" << std::endl;
    // }
    // else
    // {
    //     std::cout << "Errors: " << std::endl;
    //     for (auto &error : error_list)
    //     {
    //         std::cout << "Test ID: " << error.test_id << std::endl;
    //         std::cout << "Expected: " << error.expected << std::endl;
    //         std::cout << "Actual: " << error.actual << std::endl
    //                   << std::endl;
    //     }

    //     std::cout << "Errors number: " << error_list.size() << std::endl;
    // }

    std::cin >> N >> k >> a >> b >> S;

    std::cout << N << k << a << b << S << std::endl;

    std::cout << ChatBBB(k, a, b, S) << std::endl;

    return 0;
}