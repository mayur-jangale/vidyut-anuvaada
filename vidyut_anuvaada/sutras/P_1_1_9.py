# Sutra प.1.1.9: तुल्यास्यप्रयत्नं सवर्णम्
# Letters with same place of articulation and same effort are called savarṇa

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.9"
SUTRA_TEXT = "तुल्यास्यप्रयत्नं सवर्णम्"
SUTRA_DESC = "Letters with same place of articulation and same effort are called savarṇa"


class Sutra119:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_9
		return apply_1_1_9(word, pos)

	EXAMPLES = [
		('अग्नि', '', 'savarṇa-pairs=none'),
		('कव्य', '', 'savarṇa-pairs=none'),
		('अन्तः', '', 'savarṇa-pairs=none'),
		('वाण', '', 'savarṇa-pairs=none'),
	]

