#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
#define point pair<int, int>
#define vb vector<bool>
#define vvb vector<vb>
#define vi vector<int>
#define vvi vector<vi>


int direction_x[] = {0, 0, -1, 1};
int direction_y[] = {1, -1, 0, 0};

void DFS(int x, int y, int m, int n, vvi &picture, vvb &visited, int &size) {

    size++;
    queue<point > q;
    int cur_color = picture[x][y];
    for (int i = 0; i < 4; i++) {
        int next_x = x + direction_x[i];
        int next_y = y + direction_y[i];
        if (next_x < m && next_y < n && next_x >= 0 && next_y >= 0) {

            if (!visited[next_x][next_y] && cur_color == picture[next_x][next_y]) {
                ////////////// # 크게 배운 것 # /////////////////
                // 해당 방문 노드의 시점에서 오류가 발생하였음.
                // 처음에는 DFS호출이 되자마자 방문 처리를 하였으나,
                // 방문할 노드를 미리 방문처리 하지 않으면 다음 좌표의 DFS가 실행되기 전에, 다시 큐에 담는 작업을 반복함으로써
                // 이미 큐에 담겨있기 때문에 이미 방문한 노드를 다시 방문하는 현상이 발생.
                // 따라서 방문시점을 해당 시점으로 변경함
                visited[next_x][next_y] = true;
                q.push(point(next_x, next_y));
            }
        }
    }

    while (!q.empty()) {
        point p = q.front();
        q.pop();
        DFS(p.first, p.second, m, n, picture, visited, size);
    }
}


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vvi picture) {
    // 방문 벡터, 모두 방문하지 않음으로 초기화
    vvb visited(m, vb(n,false));

    int number_of_area = 0;
    vi area_size;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] && !visited[i][j]) { // 0인 색과 이미 방문한 노드는 방문하지 않음.
                number_of_area++; // DFS를 solution에서 호출한 횟수가, 영역의 개수 즉 connected_component
                visited[i][j] = true; // 각 영역의 첫 노드는 방문처리 해야 함. DFS의 방문 처리 기준이 DFS 실행이 아닌 큐에 담는 순간이기 때문에 첫 노드를 지정하지 않으면 방문되지 않음.
                area_size.push_back(0); // 영역이 새로 늘 때마다 영역의 크기를 담는 요소를 하나씩 추가.
                DFS(i, j, m, n, picture, visited, area_size[area_size.size() - 1]);

            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = *max_element(area_size.begin(), area_size.end());
    return answer;
}

int main() {
    vvi picture = {{1, 1, 1, 0},
                   {1, 1, 1, 0},
                   {0, 0, 0, 1},
                   {0, 0, 0, 1},
                   {0, 0, 0, 1},
                   {0, 0, 0, 1}};
    for (auto &sol: solution(6, 4, picture)) {
        cout << sol;
    }
    return 0;
}