# Sutra प.7.3.15: संख्यायाः संवत्सरसंख्यस्य च
# (Taddhita (secondary derivations)) — saMKyAyAH saMvatsarasaMKyasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.15"
SUTRA_TEXT = "संख्यायाः संवत्सरसंख्यस्य च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — saMKyAyAH saMvatsarasaMKyasya ca"


class Sutra7315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.15: अग्निः'),
		('रामः', '', 'प.7.3.15: रामः'),
		('सीता', '', 'प.7.3.15: सीता'),
	]

