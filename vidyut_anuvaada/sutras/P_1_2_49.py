# Sutra प.1.2.49: लुक् तद्धितलुकि
# (Samjna (technical definitions)) — luk tadDitaluki

from P_1_2 import apply_1_2_49

SUTRA_CODE = "प.1.2.49"
SUTRA_TEXT = "लुक् तद्धितलुकि"
SUTRA_DESC = "(Samjna (technical definitions)) — luk tadDitaluki"


class Sutra1249:
	def apply(self, word, pos):
		return apply_1_2_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-taddhita-luk:अग्निः'),
		('रामः', '', 'non-taddhita-luk:रामः'),
		('सीता', '', 'non-taddhita-luk:सीता'),
	]

