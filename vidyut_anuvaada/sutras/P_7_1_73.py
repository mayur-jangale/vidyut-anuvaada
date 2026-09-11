# Sutra प.7.1.73: इकोऽचि विभक्तौ
# (Taddhita (secondary derivations)) — iko'ci viBaktO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.73"
SUTRA_TEXT = "इकोऽचि विभक्तौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — iko'ci viBaktO"


class Sutra7173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.73: अग्निः'),
		('रामः', '', 'प.7.1.73: रामः'),
		('सीता', '', 'प.7.1.73: सीता'),
	]

