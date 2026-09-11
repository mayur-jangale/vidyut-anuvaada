# Sutra प.2.3.65: कर्तृकर्मणोः कृति
# (Samasa (compound formation)) — kartfkarmaRoH kfti

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.65"
SUTRA_TEXT = "कर्तृकर्मणोः कृति"
SUTRA_DESC = "(Samasa (compound formation)) — kartfkarmaRoH kfti"


class Sutra2365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

