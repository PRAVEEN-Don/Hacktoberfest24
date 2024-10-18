#include <iostream>
#include <vector>
using namespace std;

int trap(vector<int>& height) {
    if (height.empty()) return 0;

    int left = 0, right = height.size() - 1;
    int leftMax = 0, rightMax = 0;
    int waterTrapped = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left]; 
            } else {
                waterTrapped += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right]; 
            } else {
                waterTrapped += rightMax - height[right];
            }
            right--;
        }
    }

    return waterTrapped;
}

int main() {
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}; 
    int result = trap(height);
    cout << "The amount of water trapped is: " << result << " units." << endl;
    return 0;
}
