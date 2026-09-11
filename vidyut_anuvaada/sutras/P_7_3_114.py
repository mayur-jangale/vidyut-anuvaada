# Sutra प.7.3.114: सर्वनाम्नः स्याड्ढ्रस्वश्च
# (Taddhita (secondary derivations)) — sarvanAmnaH syAqQrasvaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.114"
SUTRA_TEXT = "सर्वनाम्नः स्याड्ढ्रस्वश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sarvanAmnaH syAqQrasvaSca"


class Sutra73114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.114: अग्निः'),
		('रामः', '', 'प.7.3.114: रामः'),
		('सीता', '', 'प.7.3.114: सीता'),
	]

