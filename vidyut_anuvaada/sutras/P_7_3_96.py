# Sutra प.7.3.96: अस्तिसिचोऽपृक्ते
# (Taddhita (secondary derivations)) — astisico'pfkte

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.96"
SUTRA_TEXT = "अस्तिसिचोऽपृक्ते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — astisico'pfkte"


class Sutra7396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.96: अग्निः'),
		('रामः', '', 'प.7.3.96: रामः'),
		('सीता', '', 'प.7.3.96: सीता'),
	]

