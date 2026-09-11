# Sutra प.5.2.19: अश्वस्यैकाहगमः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aSvasyEkAhagamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.19"
SUTRA_TEXT = "अश्वस्यैकाहगमः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aSvasyEkAhagamaH"


class Sutra5219:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.19: अग्निः'),
		('रामः', '', 'प.5.2.19: रामः'),
		('सीता', '', 'प.5.2.19: सीता'),
	]

