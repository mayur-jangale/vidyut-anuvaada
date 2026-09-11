# Sutra प.6.1.63: पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु
# sandhi-sūtra प.6.1.63

from P_6_1 import apply_6_1_63

SUTRA_CODE = "प.6.1.63"
SUTRA_TEXT = "पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु"
SUTRA_DESC = "sandhi-sūtra प.6.1.63"


class Sutra6163:
	def apply(self, word, pos):
		return apply_6_1_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.63:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.63:marker=padartha;input=रामः'),
		('सीता', '', '6.1.63:marker=padartha;input=सीता'),
	]
