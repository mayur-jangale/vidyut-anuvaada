# Sutra प.5.3.101: वस्तेर्ढञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vasterQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.101"
SUTRA_TEXT = "वस्तेर्ढञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vasterQaY"


class Sutra53101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.101: अग्निः'),
		('रामः', '', 'प.5.3.101: रामः'),
		('सीता', '', 'प.5.3.101: सीता'),
	]

