# Sutra प.5.1.62: त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — triMSaccatvAriMSatorbrAhmaRe saMjYAyAM qaR

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.62"
SUTRA_TEXT = "त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — triMSaccatvAriMSatorbrAhmaRe saMjYAyAM qaR"


class Sutra5162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.62: अग्निः'),
		('रामः', '', 'प.5.1.62: रामः'),
		('सीता', '', 'प.5.1.62: सीता'),
	]

