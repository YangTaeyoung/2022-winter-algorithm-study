#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

bool compare(int d1, int d2, char oper) {
    if (oper == '=') {
        return d1 == d2;
    } else if (oper == '>') {
        return d1 > d2;
    } else {
        return d1 < d2;
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
bool checkCondition(string friendLine, vector<string> conditions) {
    for (auto &e: conditions) {
        pair<int, int> friendsidx = make_pair(friendLine.find(e[0]), friendLine.find(e[2]));
        int real_distance = abs(friendsidx.first - friendsidx.second) - 1;
        if (!compare(real_distance, (int)e[4]-'0', e[3])){
             return false;
        }
    }
    return true;
}

int solution(int n, vector<string> data) {
    string friends = "ACFJMNRT";
    int answer = 0;
    do {
        if (checkCondition(friends, data)) {
            cout << friends << endl;
            answer++;
        }
    } while (next_permutation(friends.begin(), friends.end()));
    return answer;
}

int main() {
    cout << solution(2, vector<string>({"N~F=0", "R~T>2"})) << endl;
    return 0;
}