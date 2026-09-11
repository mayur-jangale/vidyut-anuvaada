# Sutra प.5.4.107: अव्ययीभावे शरत्प्रभृतिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyayIBAve SaratpraBftiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.107"
SUTRA_TEXT = "अव्ययीभावे शरत्प्रभृतिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyayIBAve SaratpraBftiByaH"


class Sutra54107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.107: अग्निः'),
		('रामः', '', 'प.5.4.107: रामः'),
		('सीता', '', 'प.5.4.107: सीता'),
	]

