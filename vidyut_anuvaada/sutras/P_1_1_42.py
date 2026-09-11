# Sutra प.1.1.42: शि सर्वनामस्थानम्
# (Samjna (technical definitions)) — Si sarvanAmasTAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.42"
SUTRA_TEXT = "शि सर्वनामस्थानम्"
SUTRA_DESC = "(Samjna (technical definitions)) — Si sarvanAmasTAnam"


class Sutra1142:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_42
		return apply_1_1_42(word, pos)

	EXAMPLES = [
		('शि', '', 'प.1.1.42:शि-sarvanāmasthānam;input=शि'),
		('अग्नि', '', 'प.1.1.42:शि-sarvanāmasthānam;input=अग्नि'),
	]

