# Sutra प.1.4.38: क्रुधद्रुहोरुपसृष्टयोः कर्म
# (Samjna (technical definitions)) — kruDadruhorupasfzwayoH karma

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.38"
SUTRA_TEXT = "क्रुधद्रुहोरुपसृष्टयोः कर्म"
SUTRA_DESC = "(Samjna (technical definitions)) — kruDadruhorupasfzwayoH karma"


class Sutra1438:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_38
		return apply_1_4_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-upasfzwa-karman:अग्निः'),
		('रामः', '', 'not-upasfzwa-karman:रामः'),
		('सीता', '', 'not-upasfzwa-karman:सीता'),
	]

