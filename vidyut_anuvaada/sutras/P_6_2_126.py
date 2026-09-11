# Sutra प.6.2.126: चेलखेटकटुककाण्डं गर्हायाम्
# (Sandhi (euphonic combination)) — celaKewakawukakARqaM garhAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.126"
SUTRA_TEXT = "चेलखेटकटुककाण्डं गर्हायाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — celaKewakawukakARqaM garhAyAm"


class Sutra62126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.126: अग्निः'),
		('रामः', '', 'प.6.2.126: रामः'),
		('सीता', '', 'प.6.2.126: सीता'),
	]

