# Sutra प.8.1.19: आमन्त्रितस्य च
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.19"
SUTRA_TEXT = "आमन्त्रितस्य च"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.19: अग्निः'),
		('रामः', '', 'प.8.1.19: रामः'),
		('सीता', '', 'प.8.1.19: सीता'),
	]

