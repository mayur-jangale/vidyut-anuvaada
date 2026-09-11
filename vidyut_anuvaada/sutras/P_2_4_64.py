# Sutra प.2.4.64: यञञोश्च
# (Samasa (compound formation)) — yaYaYoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.64"
SUTRA_TEXT = "यञञोश्च"
SUTRA_DESC = "(Samasa (compound formation)) — yaYaYoSca"


class Sutra2464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

