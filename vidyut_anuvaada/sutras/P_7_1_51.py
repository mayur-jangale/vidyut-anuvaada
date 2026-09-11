# Sutra प.7.1.51: अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि
# (Taddhita (secondary derivations)) — aSvakzIravfzalavaRAnAmAtmaprItO kyaci

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.51"
SUTRA_TEXT = "अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aSvakzIravfzalavaRAnAmAtmaprItO kyaci"


class Sutra7151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.51: अग्निः'),
		('रामः', '', 'प.7.1.51: रामः'),
		('सीता', '', 'प.7.1.51: सीता'),
	]

