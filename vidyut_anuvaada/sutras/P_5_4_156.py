# Sutra प.5.4.156: ईयसश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — IyasaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.156"
SUTRA_TEXT = "ईयसश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — IyasaSca"


class Sutra54156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.156: अग्निः'),
		('रामः', '', 'प.5.4.156: रामः'),
		('सीता', '', 'प.5.4.156: सीता'),
	]

