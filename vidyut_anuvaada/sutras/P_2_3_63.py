# Sutra प.2.3.63: यजेश्च करणे
# (Samasa (compound formation)) — yajeSca karaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.63"
SUTRA_TEXT = "यजेश्च करणे"
SUTRA_DESC = "(Samasa (compound formation)) — yajeSca karaRe"


class Sutra2363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

