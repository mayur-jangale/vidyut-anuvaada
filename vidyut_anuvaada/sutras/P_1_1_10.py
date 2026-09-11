# Sutra प.1.1.10: नाज्झलौ
# A sibilant followed by a cerebralsibilant is savarṇa (not applicable)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.10"
SUTRA_TEXT = "नाज्झलौ"
SUTRA_DESC = "A sibilant followed by a cerebralsibilant is savarṇa (not applicable)"


class Sutra1110:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_10
		return apply_1_1_10(word, pos)

	EXAMPLES = [
		('शष', '', 'non-savarna-pair:शष'),
		('अग्नि', '', 'savarṇa-pairs=none'),
	]

