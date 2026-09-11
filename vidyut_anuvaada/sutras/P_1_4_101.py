# Sutra प.1.4.101: तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः
# (Samjna (technical definitions)) — tiNastrIRi trIRi praTamamaDyamottamAH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.101"
SUTRA_TEXT = "तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः"
SUTRA_DESC = "(Samjna (technical definitions)) — tiNastrIRi trIRi praTamamaDyamottamAH"


class Sutra14101:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_101
		return apply_1_4_101(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-person:अग्निः'),
		('रामः', '', 'no-person:रामः'),
		('सीता', '', 'no-person:सीता'),
	]

