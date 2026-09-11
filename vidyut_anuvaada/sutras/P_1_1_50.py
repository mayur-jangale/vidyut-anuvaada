# Sutra प.1.1.50: स्थानेऽन्तरतमः
# (Samjna (technical definitions)) — sTAne'ntaratamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.50"
SUTRA_TEXT = "स्थानेऽन्तरतमः"
SUTRA_DESC = "(Samjna (technical definitions)) — sTAne'ntaratamaH"


class Sutra1150:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_50
		return apply_1_1_50(word, pos)

	EXAMPLES = [
		('अन्तरतम', '', "प.1.1.50:sthāne'ntaratamaḥ;input=अन्तरतम"),
		('अग्नि', '', "प.1.1.50:sthāne'ntaratamaḥ;input=अग्नि"),
	]

