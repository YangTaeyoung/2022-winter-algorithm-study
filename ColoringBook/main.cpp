#include <vector>
using namespace std;
#define vii vector<pair<int, int>>
#define vb vector<bool>
#define vvb vector<vb>
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    vvb visited(m, vb(n));
    fill(visited.begin(), visited.end(), vb(n, false));
    vii area;

    int cur_area_num = 0;

    int number_of_area = 0;
    int max_size_of_one_area = 0;
    for(int i = 0; i < m; i++){
        for(int i = 0; i < n; j++)
            if(picture[i][j] == 0){
                continue;
            }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}