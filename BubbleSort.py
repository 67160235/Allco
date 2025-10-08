class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def display(self):
        return f"Current data: {self.data}"

    def sort(self):
        for i in range(len(self.data)-1):
            for j in range(0, len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
            print(f"After round{i+1}: {self.data}")

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting: ")
    print(sorter.display())

    sorter.sort()

    print("After sorting: ")
    print(sorter.display())
