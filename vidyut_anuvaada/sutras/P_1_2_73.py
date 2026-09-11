# Sutra प.1.2.73: ग्राम्यपशुसंघेष्वतरुणेषु स्त्री
# (Samjna (technical definitions)) — grAmyapaSusaMGezvataruRezu strI

from P_1_2 import apply_1_2_73

SUTRA_CODE = "प.1.2.73"
SUTRA_TEXT = "ग्राम्यपशुसंघेष्वतरुणेषु स्त्री"
SUTRA_DESC = "(Samjna (technical definitions)) — grAmyapaSusaMGezvataruRezu strI"


class Sutra1273:
	def apply(self, word, pos):
		return apply_1_2_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-ataruṇa:अग्निः'),
		('रामः', '', 'non-ataruṇa:रामः'),
		('सीता', '', 'non-ataruṇa:सीता'),
	]

