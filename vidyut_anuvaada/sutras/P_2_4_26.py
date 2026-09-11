# Sutra प.2.4.26: परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः
# (Samasa (compound formation)) — paravalliNgaM dvandvatatpuruzayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.26"
SUTRA_TEXT = "परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः"
SUTRA_DESC = "(Samasa (compound formation)) — paravalliNgaM dvandvatatpuruzayoH"


class Sutra2426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

