# Sutra प.1.2.1: गाङ्कुटादिभ्योऽञ्णिन्ङित्
# (Samjna (technical definitions)) — gANkuwAdiByo'YRinNit

from P_1_2 import apply_1_2_1

SUTRA_CODE = "प.1.2.1"
SUTRA_TEXT = "गाङ्कुटादिभ्योऽञ्णिन्ङित्"
SUTRA_DESC = "(Samjna (technical definitions)) — gANkuwAdiByo'YRinNit"


class Sutra121:
	def apply(self, word, pos):
		return apply_1_2_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-gāṅkuṭādi:अग्निः'),
		('रामः', '', 'non-gāṅkuṭādi:रामः'),
		('सीता', '', 'non-gāṅkuṭādi:सीता'),
	]

