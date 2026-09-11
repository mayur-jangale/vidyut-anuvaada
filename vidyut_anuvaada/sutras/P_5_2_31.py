# Sutra प.5.2.31: नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nate nAsikAyAH saMjYAyAM wIwaYnAwajBrawacaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.31"
SUTRA_TEXT = "नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nate nAsikAyAH saMjYAyAM wIwaYnAwajBrawacaH"


class Sutra5231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.31: अग्निः'),
		('रामः', '', 'प.5.2.31: रामः'),
		('सीता', '', 'प.5.2.31: सीता'),
	]

