# Sutra प.5.4.160: निष्प्रवाणिश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nizpravARiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.160"
SUTRA_TEXT = "निष्प्रवाणिश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nizpravARiSca"


class Sutra54160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.160: अग्निः'),
		('रामः', '', 'प.5.4.160: रामः'),
		('सीता', '', 'प.5.4.160: सीता'),
	]

