# Sutra प.1.1.15: ओत्
# Ot — the augment उत् is added to certain roots

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.15"
SUTRA_TEXT = "ओत्"
SUTRA_DESC = "Ot — the augment उत् is added to certain roots"


class Sutra1115:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_15
		return apply_1_1_15(word, pos)

	EXAMPLES = [
		('उत्', '', 'ot-augmented:उत्'),
		('अग्नि', '', 'no-ot:अग्नि'),
	]

