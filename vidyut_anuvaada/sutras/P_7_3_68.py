# Sutra प.7.3.68: प्रयोज्यनियोज्यौ शक्यार्थे
# (Taddhita (secondary derivations)) — prayojyaniyojyO SakyArTe

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.68"
SUTRA_TEXT = "प्रयोज्यनियोज्यौ शक्यार्थे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — prayojyaniyojyO SakyArTe"


class Sutra7368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.68: अग्निः'),
		('रामः', '', 'प.7.3.68: रामः'),
		('सीता', '', 'प.7.3.68: सीता'),
	]

