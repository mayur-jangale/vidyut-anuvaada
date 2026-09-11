# Sutra प.5.1.42: तस्येश्वरः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasyeSvaraH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.42"
SUTRA_TEXT = "तस्येश्वरः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasyeSvaraH"


class Sutra5142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.42: अग्निः'),
		('रामः', '', 'प.5.1.42: रामः'),
		('सीता', '', 'प.5.1.42: सीता'),
	]

