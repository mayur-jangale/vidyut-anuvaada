# Sutra प.2.3.55: आशिषि नाथः
# (Samasa (compound formation)) — ASizi nATaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.55"
SUTRA_TEXT = "आशिषि नाथः"
SUTRA_DESC = "(Samasa (compound formation)) — ASizi nATaH"


class Sutra2355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

