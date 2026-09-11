# Sutra प.1.1.49: षष्ठी स्थानेयोगा
# (Samjna (technical definitions)) — zazWI sTAneyogA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.49"
SUTRA_TEXT = "षष्ठी स्थानेयोगा"
SUTRA_DESC = "(Samjna (technical definitions)) — zazWI sTAneyogA"


class Sutra1149:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_49
		return apply_1_1_49(word, pos)

	EXAMPLES = [
		('षष्ठी', '', 'प.1.1.49:ṣaṣṭhī-sthāneyogā;input=षष्ठी'),
		('अग्नि', '', 'प.1.1.49:ṣaṣṭhī-sthāneyogā;input=अग्नि'),
	]

