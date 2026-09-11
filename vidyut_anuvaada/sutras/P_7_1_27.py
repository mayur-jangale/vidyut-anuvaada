# Sutra प.7.1.27: युष्मदस्मद्भ्यां ङसोऽश्
# (Taddhita (secondary derivations)) — yuzmadasmadByAM Naso'S

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.27"
SUTRA_TEXT = "युष्मदस्मद्भ्यां ङसोऽश्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yuzmadasmadByAM Naso'S"


class Sutra7127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.27: अग्निः'),
		('रामः', '', 'प.7.1.27: रामः'),
		('सीता', '', 'प.7.1.27: सीता'),
	]

