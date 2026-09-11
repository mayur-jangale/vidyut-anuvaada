# Sutra प.1.2.40: उदात्तस्वरितपरस्य सन्नतरः
# (Samjna (technical definitions)) — udAttasvaritaparasya sannataraH

from P_1_2 import apply_1_2_40

SUTRA_CODE = "प.1.2.40"
SUTRA_TEXT = "उदात्तस्वरितपरस्य सन्नतरः"
SUTRA_DESC = "(Samjna (technical definitions)) — udAttasvaritaparasya sannataraH"


class Sutra1240:
	def apply(self, word, pos):
		return apply_1_2_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-ud-sv-para:अग्निः'),
		('रामः', '', 'non-ud-sv-para:रामः'),
		('सीता', '', 'non-ud-sv-para:सीता'),
	]

