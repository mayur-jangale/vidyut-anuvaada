# Sutra प.4.3.56: दृतिकुक्षिकलशिवस्त्यस्त्यहेर्ढञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dftikukzikalaSivastyastyaherQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.56"
SUTRA_TEXT = "दृतिकुक्षिकलशिवस्त्यस्त्यहेर्ढञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dftikukzikalaSivastyastyaherQaY"


class Sutra4356:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.56: अग्निः'),
		('रामः', '', 'प.4.3.56: रामः'),
		('सीता', '', 'प.4.3.56: सीता'),
	]

