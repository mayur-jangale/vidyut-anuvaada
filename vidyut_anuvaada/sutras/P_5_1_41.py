# Sutra प.5.1.41: सर्वभूमिपृथिवीभ्यामणञौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvaBUmipfTivIByAmaRaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.41"
SUTRA_TEXT = "सर्वभूमिपृथिवीभ्यामणञौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvaBUmipfTivIByAmaRaYO"


class Sutra5141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.41: अग्निः'),
		('रामः', '', 'प.5.1.41: रामः'),
		('सीता', '', 'प.5.1.41: सीता'),
	]

