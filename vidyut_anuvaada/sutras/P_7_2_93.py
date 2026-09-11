# Sutra प.7.2.93: यूयवयौ जसि
# (Taddhita (secondary derivations)) — yUyavayO jasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.93"
SUTRA_TEXT = "यूयवयौ जसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yUyavayO jasi"


class Sutra7293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.93: अग्निः'),
		('रामः', '', 'प.7.2.93: रामः'),
		('सीता', '', 'प.7.2.93: सीता'),
	]

