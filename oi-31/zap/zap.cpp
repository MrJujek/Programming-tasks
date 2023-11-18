#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

struct lecture
{
    int start;
    int end;
    int id;
};

bool compareByEnd(const lecture &a, const lecture &b)
{
    return a.end < b.end;
}

int main()
{
    int k;
    cin >> k;

    int start, end;
    cin >> start >> end;

    vector<lecture> lectureList = {{start, end, 0}};

    int minIndex = 0;
    int minVal = end;
    for (int i = 1; i < k; i++)
    {
        cin >> start >> end;

        if (end < minVal)
        {
            minIndex = i;
            minVal = end;
        }

        lectureList.push_back({start, end, i});
    }

    sort(lectureList.begin(), lectureList.end(), [](lecture a, lecture b)
         { return a.end < b.end; });

    vector<array<int, 2>> choosedLectures = {{minIndex, minIndex + 1}};

    for (int i = minIndex; i < k; i++)
    {
        choosedLectures.push_back({lectureList[i].id, lectureList[i + 1].id});
    }

    cout << "---- END OF INPUT ----\n";

    for (int i = 0; i < k; i++)
    {
        cout << "i: " << i << ", id: " << lectureList[i].id << ", start: " << lectureList[i].start << ", end: " << lectureList[i].end << "\n";
    }

    cout << "---- END OF LECTURE LIST ----\n";

    // sort(lectureList.begin(), lectureList.end(), compareByEnd);

    // cout << "minEnd: " << minVal << "\n";
    // cout << "minIndex: " << minIndex << "\n";

    return 0;
}