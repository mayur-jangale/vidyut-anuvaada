# Sutra प.1.4.83: कर्मप्रवचनीयाः
# (Samjna (technical definitions)) — karmapravacanIyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.83"
SUTRA_TEXT = "कर्मप्रवचनीयाः"
SUTRA_DESC = "(Samjna (technical definitions)) — karmapravacanIyAH"


class Sutra1483:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_83
		return apply_1_4_83(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-karmapravacanIya:अग्निः'),
		('रामः', '', 'not-karmapravacanIya:रामः'),
		('सीता', '', 'not-karmapravacanIya:सीता'),
	]

