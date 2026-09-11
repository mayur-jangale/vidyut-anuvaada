# Sutra प.5.4.135: गन्धस्येदुत्पूतिसुसुरभिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ganDasyedutpUtisusuraBiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.135"
SUTRA_TEXT = "गन्धस्येदुत्पूतिसुसुरभिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ganDasyedutpUtisusuraBiByaH"


class Sutra54135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.135: अग्निः'),
		('रामः', '', 'प.5.4.135: रामः'),
		('सीता', '', 'प.5.4.135: सीता'),
	]

