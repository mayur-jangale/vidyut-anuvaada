# Sutra प.7.1.36: विदेः शतुर्वसुः
# (Taddhita (secondary derivations)) — videH SaturvasuH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.36"
SUTRA_TEXT = "विदेः शतुर्वसुः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — videH SaturvasuH"


class Sutra7136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.36: अग्निः'),
		('रामः', '', 'प.7.1.36: रामः'),
		('सीता', '', 'प.7.1.36: सीता'),
	]

