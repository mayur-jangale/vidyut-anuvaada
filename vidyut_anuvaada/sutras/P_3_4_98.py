# Sutra प.3.4.98: स उत्तमस्य
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sa uttamasya

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.98"
SUTRA_TEXT = "स उत्तमस्य"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sa uttamasya"


class Sutra3498:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

