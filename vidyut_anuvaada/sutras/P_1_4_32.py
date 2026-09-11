# Sutra प.1.4.32: कर्मणा यमभिप्रैति स सम्प्रदानम्
# (Samjna (technical definitions)) — karmaRA yamaBiprEti sa sampradAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.32"
SUTRA_TEXT = "कर्मणा यमभिप्रैति स सम्प्रदानम्"
SUTRA_DESC = "(Samjna (technical definitions)) — karmaRA yamaBiprEti sa sampradAnam"


class Sutra1432:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_32
		return apply_1_4_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sampradAnam:अग्निः'),
		('रामः', '', 'not-sampradAnam:रामः'),
		('सीता', '', 'not-sampradAnam:सीता'),
	]

