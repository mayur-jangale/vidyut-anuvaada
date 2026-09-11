# Sutra प.8.4.4: वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.4"
SUTRA_TEXT = "वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः"
SUTRA_DESC = "final transformations — continued"


class Sutra844:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.4: अग्निः'),
		('रामः', '', 'प.8.4.4: रामः'),
		('सीता', '', 'प.8.4.4: सीता'),
	]

