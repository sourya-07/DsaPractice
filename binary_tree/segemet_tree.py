class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)  # Enough space
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, left, right):
        if left == right:
            self.tree[index] = nums[left]
            return

        mid = (left + right) // 2
        self.build(nums, 2 * index + 1, left, mid)
        self.build(nums, 2 * index + 2, mid + 1, right)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def update(self, idx, value, index=0, left=0, right=None):
        if right is None:
            right = self.n - 1

        if left == right:
            self.tree[index] = value
            return

        mid = (left + right) // 2
        if idx <= mid:
            self.update(idx, value, 2 * index + 1, left, mid)
        else:
            self.update(idx, value, 2 * index + 2, mid + 1, right)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def query(self, l, r, index=0, left=0, right=None):
        if right is None:
            right = self.n - 1

        if l > right or r < left:
            return 0  # No overlap

        if l <= left and r >= right:
            return self.tree[index]  # Total overlap

        mid = (left + right) // 2
        left_sum = self.query(l, r, 2 * index + 1, left, mid)
        right_sum = self.query(l, r, 2 * index + 2, mid + 1, right)

        return left_sum + right_sum


arr = [1, 3, 5, 7, 9, 11]
seg = SegmentTree(arr)

print(seg.query(1, 3))  # Output: 3 + 5 + 7 = 15

seg.update(1, 10)       # arr becomes [1, 10, 5, 7, 9, 11]
print(seg.query(1, 3))  # Output: 10 + 5 + 7 = 22