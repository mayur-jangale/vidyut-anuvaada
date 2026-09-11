# Sutra प.5.3.69: प्रकारवचने जातीयर्
# gaṇa — group of (tri-gaṇa → trigaṇa)

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.69"
SUTRA_TEXT = "प्रकारवचने जातीयर्"
SUTRA_DESC = "gaṇa — group of (tri-gaṇa → trigaṇa)"


class Sutra5369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.69: अग्निः'),
		('रामः', '', 'प.5.3.69: रामः'),
		('सीता', '', 'प.5.3.69: सीता'),
	]

