# Sutra प.5.2.25: पक्षात्तिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pakzAttiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.25"
SUTRA_TEXT = "पक्षात्तिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pakzAttiH"


class Sutra5225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.25: अग्निः'),
		('रामः', '', 'प.5.2.25: रामः'),
		('सीता', '', 'प.5.2.25: सीता'),
	]

