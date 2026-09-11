# Sutra प.5.2.138: कंशंभ्यां बभयुस्तितुतयसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaMSaMByAM baBayustitutayasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.138"
SUTRA_TEXT = "कंशंभ्यां बभयुस्तितुतयसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaMSaMByAM baBayustitutayasaH"


class Sutra52138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.138: अग्निः'),
		('रामः', '', 'प.5.2.138: रामः'),
		('सीता', '', 'प.5.2.138: सीता'),
	]

