# Sutra प.5.4.102: द्वित्रिभ्यामञ्जलेः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAmaYjaleH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.102"
SUTRA_TEXT = "द्वित्रिभ्यामञ्जलेः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAmaYjaleH"


class Sutra54102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.102: अग्निः'),
		('रामः', '', 'प.5.4.102: रामः'),
		('सीता', '', 'प.5.4.102: सीता'),
	]

