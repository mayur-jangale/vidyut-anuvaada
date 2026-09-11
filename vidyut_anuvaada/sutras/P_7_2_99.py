# Sutra प.7.2.99: त्रिचतुरोः स्त्रियां तिसृचतसृ
# (Taddhita (secondary derivations)) — tricaturoH striyAM tisfcatasf

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.99"
SUTRA_TEXT = "त्रिचतुरोः स्त्रियां तिसृचतसृ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tricaturoH striyAM tisfcatasf"


class Sutra7299:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.99: अग्निः'),
		('रामः', '', 'प.7.2.99: रामः'),
		('सीता', '', 'प.7.2.99: सीता'),
	]

