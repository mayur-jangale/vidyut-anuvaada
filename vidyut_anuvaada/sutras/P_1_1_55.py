# Sutra प.1.1.55: अनेकाल्शित्सर्वस्य
# (Samjna (technical definitions)) — anekAlSitsarvasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.55"
SUTRA_TEXT = "अनेकाल्शित्सर्वस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — anekAlSitsarvasya"


class Sutra1155:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_55
		return apply_1_1_55(word, pos)

	EXAMPLES = [
		('अनेक', '', 'प.1.1.55:anekālśit-sarvasya;input=अनेक'),
		('अग्नि', '', 'प.1.1.55:anekālśit-sarvasya;input=अग्नि'),
	]

