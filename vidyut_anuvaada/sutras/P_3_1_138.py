# Sutra प.3.1.138: अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anupasargAllimpavindaDAripArivedyudejicetisAtisAhiByaSca

from P_3_1 import apply_3_1_138

SUTRA_CODE = "प.3.1.138"
SUTRA_TEXT = "अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anupasargAllimpavindaDAripArivedyudejicetisAtisAhiByaSca"


class Sutra31138:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_138(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.138:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.138:root=रामः;pos='),
		('सीता', '', 'प.3.1.138:root=सीता;pos='),
	]

