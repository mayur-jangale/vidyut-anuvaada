# Sutra प.3.2.150: जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jucaNkramyadandramyasfgfDijvalaSucalazapatapadaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.150"
SUTRA_TEXT = "जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jucaNkramyadandramyasfgfDijvalaSucalazapatapadaH"


class Sutra32150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

