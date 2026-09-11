# Sutra प.5.1.108: प्रकृष्टे ठञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prakfzwe WaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.108"
SUTRA_TEXT = "प्रकृष्टे ठञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prakfzwe WaY"


class Sutra51108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.108: अग्निः'),
		('रामः', '', 'प.5.1.108: रामः'),
		('सीता', '', 'प.5.1.108: सीता'),
	]

