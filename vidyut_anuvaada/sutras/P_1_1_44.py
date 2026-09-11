# Sutra प.1.1.44: न वेति विभाषा
# (Samjna (technical definitions)) — na veti viBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.44"
SUTRA_TEXT = "न वेति विभाषा"
SUTRA_DESC = "(Samjna (technical definitions)) — na veti viBAzA"


class Sutra1144:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_44
		return apply_1_1_44(word, pos)

	EXAMPLES = [
		('वा', '', 'प.1.1.44:na-ve-ti-viBHāṣā;input=वा'),
		('अग्नि', '', 'प.1.1.44:na-ve-ti-viBHāṣā;input=अग्नि'),
	]

