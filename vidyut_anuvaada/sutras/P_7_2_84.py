# Sutra प.7.2.84: अष्टन आ विभक्तौ
# (Taddhita (secondary derivations)) — azwana A viBaktO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.84"
SUTRA_TEXT = "अष्टन आ विभक्तौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — azwana A viBaktO"


class Sutra7284:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.84: अग्निः'),
		('रामः', '', 'प.7.2.84: रामः'),
		('सीता', '', 'प.7.2.84: सीता'),
	]

