# Sutra प.5.3.32: पश्चात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paScAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.32"
SUTRA_TEXT = "पश्चात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paScAt"


class Sutra5332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.32: अग्निः'),
		('रामः', '', 'प.5.3.32: रामः'),
		('सीता', '', 'प.5.3.32: सीता'),
	]

