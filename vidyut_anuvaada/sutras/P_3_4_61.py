# Sutra प.3.4.61: स्वाङ्गे तस्प्रत्यये कृभ्वोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — svANge taspratyaye kfBvoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.61"
SUTRA_TEXT = "स्वाङ्गे तस्प्रत्यये कृभ्वोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — svANge taspratyaye kfBvoH"


class Sutra3461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

