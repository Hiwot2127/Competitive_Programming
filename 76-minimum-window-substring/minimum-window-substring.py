class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1

        left = 0
        right = 0
        min_window_size = float('inf')
        min_window_start = 0
        target_count = len(target_counts)

        while right < len(s):
            if s[right] in target_counts:
                target_counts[s[right]] -= 1
                if target_counts[s[right]] == 0:
                    target_count -= 1

            while target_count == 0:
                if min_window_size > right - left + 1:
                    min_window_size = right - left + 1
                    min_window_start = left

                if s[left] in target_counts:
                    target_counts[s[left]] += 1
                    if target_counts[s[left]] > 0:
                        target_count += 1

                left += 1

            right += 1

        if min_window_size == float('inf'):
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_size]