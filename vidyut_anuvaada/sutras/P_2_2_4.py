# Sutra प.2.2.4: प्राप्तापन्ने च द्वितीयया
# (Samasa (compound formation)) — prAptApanne ca dvitIyayA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.4"
SUTRA_TEXT = "प्राप्तापन्ने च द्वितीयया"
SUTRA_DESC = "(Samasa (compound formation)) — prAptApanne ca dvitIyayA"


class Sutra224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

