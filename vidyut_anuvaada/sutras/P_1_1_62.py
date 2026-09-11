# Sutra प.1.1.62: प्रत्ययलोपे प्रत्ययलक्षणम्
# (Samjna (technical definitions)) — pratyayalope pratyayalakzaRam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.62"
SUTRA_TEXT = "प्रत्ययलोपे प्रत्ययलक्षणम्"
SUTRA_DESC = "(Samjna (technical definitions)) — pratyayalope pratyayalakzaRam"


class Sutra1162:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_62
		return apply_1_1_62(word, pos)

	EXAMPLES = [
		('प्रत्यय', '', 'प.1.1.62:pratyayalope-pratyayalakṣaṇam;input=प्रत्यय'),
		('अग्नि', '', 'प.1.1.62:pratyayalope-pratyayalakṣaṇam;input=अग्नि'),
	]

