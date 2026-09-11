# Sutra प.5.3.30: अञ्चेर्लुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aYcerluk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.30"
SUTRA_TEXT = "अञ्चेर्लुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aYcerluk"


class Sutra5330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.30: अग्निः'),
		('रामः', '', 'प.5.3.30: रामः'),
		('सीता', '', 'प.5.3.30: सीता'),
	]

