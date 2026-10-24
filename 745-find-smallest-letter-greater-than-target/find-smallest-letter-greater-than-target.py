class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        s, e = 0, len(letters) - 1

        while s <= e:
            mid = s + (e - s) // 2
            if target < letters[mid]:
                e = mid - 1
            else:  # target >= letters[mid]
                s = mid + 1

        return letters[s % len(letters)]