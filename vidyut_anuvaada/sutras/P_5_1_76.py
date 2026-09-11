# Sutra प.5.1.76: पन्थो ण नित्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — panTo Ra nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.76"
SUTRA_TEXT = "पन्थो ण नित्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — panTo Ra nityam"


class Sutra5176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.76: अग्निः'),
		('रामः', '', 'प.5.1.76: रामः'),
		('सीता', '', 'प.5.1.76: सीता'),
	]

