"""Small demo: sorting tricks

Two examples:
- sort strings by number of vowels (then alphabetically)
- sort integers by digit sum (then value)

Run the file to see examples.
"""

def sort_by_vowel_count(strings):
	"""Return list of strings sorted by vowel count (asc), then alphabetically."""
	vowels = set("aeiouAEIOU")
	def vowel_count(s):
		return sum(1 for ch in s if ch in vowels)
	return sorted(strings, key=lambda s: (vowel_count(s), s.lower()))


def sort_by_digit_sum(numbers):
	"""Return list of integers sorted by sum of digits (asc), then by numeric value."""
	def digit_sum(n):
		return sum(int(d) for d in str(abs(n)))
	return sorted(numbers, key=lambda n: (digit_sum(n), n))


def _demo():
	strings = ["banana", "apple", "kiwi", "avocado", "grape", "Orange"]
	numbers = [91, 10, 34, 202, 5, 14, -23]

	print("Original strings:", strings)
	print("Sorted by vowel count:", sort_by_vowel_count(strings))
	print()
	print("Original numbers:", numbers)
	print("Sorted by digit sum:", sort_by_digit_sum(numbers))


if __name__ == '__main__':
	_demo()
print("AI is a new electricity")