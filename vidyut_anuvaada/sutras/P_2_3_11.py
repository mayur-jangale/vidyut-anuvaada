# Sutra प.2.3.11: प्रतिनिधिप्रतिदाने च यस्मात्
# (Samasa (compound formation)) — pratiniDipratidAne ca yasmAt

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.11"
SUTRA_TEXT = "प्रतिनिधिप्रतिदाने च यस्मात्"
SUTRA_DESC = "(Samasa (compound formation)) — pratiniDipratidAne ca yasmAt"


class Sutra2311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

