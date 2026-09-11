# Sutra प.2.1.34: अन्नेन व्यञ्जनम्
# marker: anna-vyañjanam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.34"
SUTRA_TEXT = "अन्नेन व्यञ्जनम्"
SUTRA_DESC = "anna-vyañjanam"


class Sutra2134:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_34
  return apply_2_1_34(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.34:anna-vyañjanam;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.34:anna-vyañjanam;input=रामः;pos='),
		('सीता', '', 'प.2.1.34:anna-vyañjanam;input=सीता;pos='),
	]
