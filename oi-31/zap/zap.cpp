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

    vector<array<int, 2>> choosedLectures = {{lectureList[0].id, lectureList[1].id}};

    // Initialize the end time of the last added lecture
    int lastEndTime = lectureList[0].end;

    // Initialize the end time of the last added lecture
    int lastEndTime = -1;

    // Start from the first lecture
    for (int i = 0; i < k; i++)
    {
        // If the start time of the current lecture is not before the end time of the last added lecture
        if (lectureList[i].start >= lastEndTime)
        {
            // Add the current lecture to the choosedLectures list
            choosedLectures.push_back(lectureList[i].id);

            // Update the end time of the last added lecture
            lastEndTime = lectureList[i].end;
        }
    }

    cout << "---- END OF INPUT ----\n";

    for (int i = 0; i < k; i++)
    {
        cout << "i: " << i << ", id: " << lectureList[i].id << ", start: " << lectureList[i].start << ", end: " << lectureList[i].end << "\n";
    }

    cout << "---- END OF LECTURE LIST ----\n";

    for (const auto &pair : choosedLectures)
    {
        cout << "Lecture Pair: " << pair[0] << ", " << pair[1] << "\n";
    }

    return 0;
}