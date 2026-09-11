# Sutra प.2.4.12: विभाषा वृक्षमृगतृणधान्यव्यञ्जनपशुशकुन्यश्ववडवपूर्वापराधरोत्तराणाम्
# (Samasa (compound formation)) — viBAzA vfkzamfgatfRaDAnyavyaYjanapaSuSakunyaSvavaqavapUrvAparADarottarARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.12"
SUTRA_TEXT = "विभाषा वृक्षमृगतृणधान्यव्यञ्जनपशुशकुन्यश्ववडवपूर्वापराधरोत्तराणाम्"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA vfkzamfgatfRaDAnyavyaYjanapaSuSakunyaSvavaqavapUrvAparADarottarARAm"


class Sutra2412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

