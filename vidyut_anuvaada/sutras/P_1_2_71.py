# Sutra प.1.2.71: श्वशुरः श्वश्र्वा
# (Samjna (technical definitions)) — SvaSuraH SvaSrvA

from P_1_2 import apply_1_2_71

SUTRA_CODE = "प.1.2.71"
SUTRA_TEXT = "श्वशुरः श्वश्र्वा"
SUTRA_DESC = "(Samjna (technical definitions)) — SvaSuraH SvaSrvA"


class Sutra1271:
	def apply(self, word, pos):
		return apply_1_2_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-śvaśura:अग्निः'),
		('रामः', '', 'non-śvaśura:रामः'),
		('सीता', '', 'non-śvaśura:सीता'),
	]

