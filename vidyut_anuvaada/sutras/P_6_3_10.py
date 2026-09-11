# Sutra प.6.3.10: कारनाम्नि च प्राचां हलादौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.10"
SUTRA_TEXT = "कारनाम्नि च प्राचां हलादौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.10: अग्निः'),
		('रामः', '', 'प.6.3.10: रामः'),
		('सीता', '', 'प.6.3.10: सीता'),
	]

