# Sutra प.5.4.146: ककुदस्यावस्थायां लोपः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kakudasyAvasTAyAM lopaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.146"
SUTRA_TEXT = "ककुदस्यावस्थायां लोपः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kakudasyAvasTAyAM lopaH"


class Sutra54146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.146: अग्निः'),
		('रामः', '', 'प.5.4.146: रामः'),
		('सीता', '', 'प.5.4.146: सीता'),
	]

