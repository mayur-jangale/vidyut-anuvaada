# Sutra प.7.3.16: वर्षस्याभविष्यति
# (Taddhita (secondary derivations)) — varzasyABavizyati

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.16"
SUTRA_TEXT = "वर्षस्याभविष्यति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — varzasyABavizyati"


class Sutra7316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.16: अग्निः'),
		('रामः', '', 'प.7.3.16: रामः'),
		('सीता', '', 'प.7.3.16: सीता'),
	]

