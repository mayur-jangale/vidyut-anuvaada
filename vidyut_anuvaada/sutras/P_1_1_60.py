# Sutra प.1.1.60: अदर्शनं लोपः
# (Samjna (technical definitions)) — adarSanaM lopaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.60"
SUTRA_TEXT = "अदर्शनं लोपः"
SUTRA_DESC = "(Samjna (technical definitions)) — adarSanaM lopaH"


class Sutra1160:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_60
		return apply_1_1_60(word, pos)

	EXAMPLES = [
		('', '', 'lopa:empty'),
		('क', '', 'lopa-applies:क'),
	]

