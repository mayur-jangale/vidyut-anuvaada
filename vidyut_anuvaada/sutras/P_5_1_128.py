# Sutra प.5.1.128: पत्यन्तपुरोहितादिभ्यो यक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — patyantapurohitAdiByo yak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.128"
SUTRA_TEXT = "पत्यन्तपुरोहितादिभ्यो यक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — patyantapurohitAdiByo yak"


class Sutra51128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.128: अग्निः'),
		('रामः', '', 'प.5.1.128: रामः'),
		('सीता', '', 'प.5.1.128: सीता'),
	]

