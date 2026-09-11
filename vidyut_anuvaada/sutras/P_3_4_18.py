# Sutra प.3.4.18: अलङ्खल्वोः प्रतिषेधयोः प्राचां क्त्वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — alaNKalvoH pratizeDayoH prAcAM ktvA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.18"
SUTRA_TEXT = "अलङ्खल्वोः प्रतिषेधयोः प्राचां क्त्वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — alaNKalvoH pratizeDayoH prAcAM ktvA"


class Sutra3418:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

