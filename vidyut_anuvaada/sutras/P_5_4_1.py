# Sutra प.5.4.1: पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdaSatasya saMKyAdervIpsAyAM vun lopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.1"
SUTRA_TEXT = "पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdaSatasya saMKyAdervIpsAyAM vun lopaSca"


class Sutra541:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.1: अग्निः'),
		('रामः', '', 'प.5.4.1: रामः'),
		('सीता', '', 'प.5.4.1: सीता'),
	]

