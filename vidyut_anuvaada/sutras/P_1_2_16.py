# Sutra प.1.2.16: विभाषोपयमने
# (Samjna (technical definitions)) — viBAzopayamane

from P_1_2 import apply_1_2_16

SUTRA_CODE = "प.1.2.16"
SUTRA_TEXT = "विभाषोपयमने"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzopayamane"


class Sutra1216:
	def apply(self, word, pos):
		return apply_1_2_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-upayamana:अग्निः'),
		('रामः', '', 'non-upayamana:रामः'),
		('सीता', '', 'non-upayamana:सीता'),
	]

