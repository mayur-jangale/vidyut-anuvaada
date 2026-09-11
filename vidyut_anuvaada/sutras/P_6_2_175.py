# Sutra प.6.2.175: बहोर्नञ्वदुत्तरपदभूम्नि
# (Sandhi (euphonic combination)) — bahornaYvaduttarapadaBUmni

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.175"
SUTRA_TEXT = "बहोर्नञ्वदुत्तरपदभूम्नि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — bahornaYvaduttarapadaBUmni"


class Sutra62175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.175: अग्निः'),
		('रामः', '', 'प.6.2.175: रामः'),
		('सीता', '', 'प.6.2.175: सीता'),
	]

