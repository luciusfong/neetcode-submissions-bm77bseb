#include <vector>
using namespace std;

class DynamicArray {
private:
    int capacity;
    int size;
    vector<int> arr;

public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        arr.resize(capacity);
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        size--;
        return arr[size];
    }

    void resize() {
        capacity *= 2;
        vector<int> newArr(capacity);

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};