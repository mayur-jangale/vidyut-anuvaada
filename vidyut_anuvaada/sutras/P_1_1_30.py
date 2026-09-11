# Sutra प.1.1.30: तृतीयासमासे
# (Samjna (technical definitions)) — tftIyAsamAse

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.30"
SUTRA_TEXT = "तृतीयासमासे"
SUTRA_DESC = "(Samjna (technical definitions)) — tftIyAsamAse"


class Sutra1130:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_30
		return apply_1_1_30(word, pos)

	EXAMPLES = [
		('देव', 'tatpurusha-tṛtīyā', 'tṛtīyā-tatpurusha:देव'),
		('देव', '', 'other-samāsa:देव'),
	]

