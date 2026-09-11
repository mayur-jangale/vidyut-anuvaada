# Sutra प.5.4.140: संख्यासुपूर्वस्य
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAsupUrvasya

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.140"
SUTRA_TEXT = "संख्यासुपूर्वस्य"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAsupUrvasya"


class Sutra54140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.140: अग्निः'),
		('रामः', '', 'प.5.4.140: रामः'),
		('सीता', '', 'प.5.4.140: सीता'),
	]

