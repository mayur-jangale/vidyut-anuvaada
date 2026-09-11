# Sutra प.5.4.68: समासान्ताः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAsAntAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.68"
SUTRA_TEXT = "समासान्ताः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAsAntAH"


class Sutra5468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.68: अग्निः'),
		('रामः', '', 'प.5.4.68: रामः'),
		('सीता', '', 'प.5.4.68: सीता'),
	]

