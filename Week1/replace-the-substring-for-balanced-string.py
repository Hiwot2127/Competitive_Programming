class Solution:
    def balancedString(self, s: str) -> int:
        extra = ""
        target = len(s) // 4
        count = Counter(s)

        for char in count:
            if count[char] > target:
                extra += (count[char] - target) * char

        if not extra:
            return 0

        extra_count = Counter(extra)
        left = 0
        min_length = inf
        window_count = Counter()

        for right, char in enumerate(s):
            window_count[char] += 1
            while extra_count - window_count == Counter():
                min_length = min(min_length, right - left + 1)
                window_count[s[left]] -= 1
                left += 1

        return min_length