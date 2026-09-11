# Sutra प.1.1.48: एच इग्घ्रस्वादेशे
# (Samjna (technical definitions)) — eca igGrasvAdeSe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.48"
SUTRA_TEXT = "एच इग्घ्रस्वादेशे"
SUTRA_DESC = "(Samjna (technical definitions)) — eca igGrasvAdeSe"


class Sutra1148:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_48
		return apply_1_1_48(word, pos)

	EXAMPLES = [
		('एङ्', '', 'प.1.1.48:eca-igghrasvādeśe;input=एङ्'),
		('अग्नि', '', 'प.1.1.48:eca-igghrasvādeśe;input=अग्नि'),
	]

