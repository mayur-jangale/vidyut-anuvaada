# Sutra प.8.1.71: तिङि चोदात्तवति
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.71"
SUTRA_TEXT = "तिङि चोदात्तवति"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.71: अग्निः'),
		('रामः', '', 'प.8.1.71: रामः'),
		('सीता', '', 'प.8.1.71: सीता'),
	]

