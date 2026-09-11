# Sutra प.7.2.54: लुभो विमोहने
# (Taddhita (secondary derivations)) — luBo vimohane

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.54"
SUTRA_TEXT = "लुभो विमोहने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — luBo vimohane"


class Sutra7254:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.54: अग्निः'),
		('रामः', '', 'प.7.2.54: रामः'),
		('सीता', '', 'प.7.2.54: सीता'),
	]

