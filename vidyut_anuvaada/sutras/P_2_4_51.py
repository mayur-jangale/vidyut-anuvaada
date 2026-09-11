# Sutra प.2.4.51: णौ च सँश्चङोः
# (Samasa (compound formation)) — RO ca sa~ScaNoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.51"
SUTRA_TEXT = "णौ च सँश्चङोः"
SUTRA_DESC = "(Samasa (compound formation)) — RO ca sa~ScaNoH"


class Sutra2451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

