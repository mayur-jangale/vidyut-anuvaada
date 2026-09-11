# Sutra प.5.3.107: शर्करादिभ्योऽण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SarkarAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.107"
SUTRA_TEXT = "शर्करादिभ्योऽण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SarkarAdiByo'R"


class Sutra53107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.107: अग्निः'),
		('रामः', '', 'प.5.3.107: रामः'),
		('सीता', '', 'प.5.3.107: सीता'),
	]

