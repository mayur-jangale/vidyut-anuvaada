# Sutra प.5.4.145: अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — agrAntaSudDaSuBravfzavarAheByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.145"
SUTRA_TEXT = "अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — agrAntaSudDaSuBravfzavarAheByaSca"


class Sutra54145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.145: अग्निः'),
		('रामः', '', 'प.5.4.145: रामः'),
		('सीता', '', 'प.5.4.145: सीता'),
	]

