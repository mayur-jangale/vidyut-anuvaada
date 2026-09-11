# Sutra प.2.4.29: रात्राह्नाहाः पुंसि
# (Samasa (compound formation)) — rAtrAhnAhAH puMsi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.29"
SUTRA_TEXT = "रात्राह्नाहाः पुंसि"
SUTRA_DESC = "(Samasa (compound formation)) — rAtrAhnAhAH puMsi"


class Sutra2429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

