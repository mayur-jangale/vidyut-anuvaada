# Sutra प.5.4.148: उद्विभ्यां काकुदस्य
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — udviByAM kAkudasya

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.148"
SUTRA_TEXT = "उद्विभ्यां काकुदस्य"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — udviByAM kAkudasya"


class Sutra54148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.148: अग्निः'),
		('रामः', '', 'प.5.4.148: रामः'),
		('सीता', '', 'प.5.4.148: सीता'),
	]

