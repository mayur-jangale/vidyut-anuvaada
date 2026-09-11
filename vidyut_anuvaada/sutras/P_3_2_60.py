# Sutra प.3.2.60: त्यदादिषु दृशोऽनालोचने कञ् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tyadAdizu dfSo'nAlocane kaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.60"
SUTRA_TEXT = "त्यदादिषु दृशोऽनालोचने कञ् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tyadAdizu dfSo'nAlocane kaY ca"


class Sutra3260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

