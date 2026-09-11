# Sutra प.1.1.16: सम्बुद्धौ शाकल्यस्येतावनार्षे
# sambodhana (vocative) of śākalya follows Vedic form

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.16"
SUTRA_TEXT = "सम्बुद्धौ शाकल्यस्येतावनार्षे"
SUTRA_DESC = "sambodhana (vocative) of śākalya follows Vedic form"


class Sutra1116:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_16
		return apply_1_1_16(word, pos)

	EXAMPLES = [
		('हे', '', 'vocalic-sambodhana:हे'),
		('अग्ने', '', 'vocalic-sambodhana:अग्ने'),
	]

