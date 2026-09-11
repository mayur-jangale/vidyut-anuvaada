# Sutra प.2.4.53: ब्रुवो वचिः
# (Samasa (compound formation)) — bruvo vaciH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.53"
SUTRA_TEXT = "ब्रुवो वचिः"
SUTRA_DESC = "(Samasa (compound formation)) — bruvo vaciH"


class Sutra2453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

