from django import forms

SORT_OPTION = (
	('1', 'Name'),
	('2', 'Personality'),
	('3', 'Gender'),
	('4', 'Birthday')
)

class SortBy(forms.Form):
	sort_options = forms.ChoiceField(choices = SORT_OPTION)