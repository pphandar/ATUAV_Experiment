from django import forms

class LocusForm(forms.Form):
	q1 =  [('A', 'Children get into trouble because their parents punish them too much.'),
		   ('B', 'The trouble with most children nowadays is that their parents are too easy with them.')]
	q2 =  [('A', 'Many of the unhappy things in people\'s lives are partly due to bad luck.'),
		   ('B', 'People\'s misfortunes result from the mistakes they make.')]
	q3 =  [('A', 'One of the major reasons why we have wars is because people don\'t take enough interest in politics.'),
		   ('B', 'There will always be wars, no matter how hard people try to prevent them.')]
	q4 =  [('A', 'In the long run people get the respect they deserve in this world.'),
		   ('B', 'Unfortunately, an individual\'s worth often passes unrecognized no matter how hard he tries.')]
	q5 =  [('A', 'The idea that teachers are unfair to students is nonsense.'),
		   ('B', 'Most students don\'t realize the extent to which their grades are influenced by accidental happenings.')]
	q6 =  [('A', 'Without the right breaks one cannot be an effective leader.'),
		   ('B', 'Capable people who fail to become leaders have not taken advantage of their opportunities.')]
	q7 =  [('A', 'No matter how hard you try some people just don\'t like you.'),
		   ('B', 'People who can\'t get others to like them don\'t understand how to get along with others.')]
	q8 =  [('A', 'Heredity plays the major role in determining one\'s personality.'),
		   ('B', 'It is one\'s experiences in life which determine what they\'re like.')]
	q9 =  [('A', 'I have often found that what is going to happen will happen.'),
		   ('B', 'Trusting to fate has never turned out as well for me as making a decision to take a definite course of action.')]
	q10 = [('A', 'In the case of the well prepared student there is rarely if ever such a thing as an unfair test.'),
		   ('B', 'Many times exam questions tend to be so unrelated to course work that studying in really useless.')]
	q11 = [('A', 'Becoming a success is a matter of hard work, luck has little or nothing to do with it.'),
		   ('B', 'Getting a good job depends mainly on being in the right place at the right time.')]
	q12 = [('A', 'The average citizen can have an influence in government decisions.'),
		   ('B', 'This world is run by the few people in power, and there is not much the little guy can do about it.')]
	q13 = [('A', 'When I make plans, I am almost certain that I can make them work.'),
		   ('B', 'It is not always wise to plan too far ahead because many things turn out to be a matter of good or bad fortune anyhow.')]
	q14 = [('A', 'There are certain people who are just no good.'),
		   ('B', 'There is some good in everybody.')]
	q15 = [('A', 'In my case getting what I want has little or nothing to do with luck.'),
		   ('B', 'Many times we might just as well decide what to do by flipping a coin.')]
	q16 = [('A', 'Who gets to be the boss often depends on who was lucky enough to be in the right place first.'),
		   ('B', 'Getting people to do the right thing depends upon ability, luck has little or nothing to do with it.')]
	q17 = [('A', 'As far as world affairs are concerned, most of us are the victims of forces we can neither understand, nor control.'),
		   ('B', 'By taking an active part in political and social affairs the people can control world events.')]
	q18 = [('A', 'Most people don\'t realize the extent to which their lives are controlled by accidental happenings.'),
		   ('B', 'There really is no such thing as "luck."')]
	q19 = [('A', 'One should always be willing to admit mistakes.'),
		   ('B', 'It is usually best to cover up one\'s mistakes.')]
	q20 = [('A', 'It is hard to know whether or not a person really likes you.'),
		   ('B', 'How many friends you have depends upon how nice a person you are.')]
	q21 = [('A', 'In the long run the bad things that happen to us are balanced by the good ones.'),
		   ('B', 'Most misfortunes are the result of lack of ability, ignorance, laziness, or all three.')]
	q22 = [('A', 'With enough effort we can wipe out political corruption.'),
		   ('B', 'It is difficult for people to have much control over the things politicians do in office.')]
	q23=  [('A', 'Sometimes I can\'t understand how teachers arrive at the grades they give.'),
		   ('B', 'There is a direct connection between how hard 1 study and the grades I get.')]
	q24 = [('A', 'A good leader expects people to decide for themselves what they should do.'),
		   ('B', 'A good leader makes it clear to everybody what their jobs are.')]
	q25 = [('A', 'Many times I feel that I have little influence over the things that happen to me.'),
		   ('B', 'It is impossible for me to believe that chance or luck plays an important role in my life.')]
	q26 = [('A', 'People are lonely because they don\'t try to be friendly.'),
		   ('B', 'There\'s not much use in trying too hard to please people, if they like you, they like you.')]
	q27 = [('A', 'There is too much emphasis on athletics in high school.'),
		   ('B', 'Team sports are an excellent way to build character.')]
	q28 = [('A', 'What happens to me is my own doing.'),
		   ('B', 'Sometimes I feel that I don\'t have enough control over the direction my life is taking.')]
	q29 = [('A', 'Most of the time I can\'t understand why politicians behave the way they do.'),
		   ('B', 'In the long run the people are responsible for bad government on a national as well as on a local level.')]
	

	question_1 = forms.ChoiceField(choices=q1, widget=forms.RadioSelect())
	question_2 = forms.ChoiceField(choices=q2, widget=forms.RadioSelect())
	question_3 = forms.ChoiceField(choices=q3, widget=forms.RadioSelect())
	question_4 = forms.ChoiceField(choices=q4, widget=forms.RadioSelect())
	question_5 = forms.ChoiceField(choices=q5, widget=forms.RadioSelect())
	question_6 = forms.ChoiceField(choices=q6, widget=forms.RadioSelect())
	question_7 = forms.ChoiceField(choices=q7, widget=forms.RadioSelect())
	question_8 = forms.ChoiceField(choices=q8, widget=forms.RadioSelect())
	question_9 = forms.ChoiceField(choices=q9, widget=forms.RadioSelect())
	question_10 = forms.ChoiceField(choices=q10, widget=forms.RadioSelect())
	question_11 = forms.ChoiceField(choices=q11, widget=forms.RadioSelect())
	question_12 = forms.ChoiceField(choices=q12, widget=forms.RadioSelect())
	question_13 = forms.ChoiceField(choices=q13, widget=forms.RadioSelect())
	question_14 = forms.ChoiceField(choices=q14, widget=forms.RadioSelect())
	question_15 = forms.ChoiceField(choices=q15, widget=forms.RadioSelect())
	question_16 = forms.ChoiceField(choices=q16, widget=forms.RadioSelect())
	question_17 = forms.ChoiceField(choices=q17, widget=forms.RadioSelect())
	question_18 = forms.ChoiceField(choices=q18, widget=forms.RadioSelect())
	question_19 = forms.ChoiceField(choices=q19, widget=forms.RadioSelect())
	question_20 = forms.ChoiceField(choices=q20, widget=forms.RadioSelect())
	question_21 = forms.ChoiceField(choices=q21, widget=forms.RadioSelect())
	question_22 = forms.ChoiceField(choices=q22, widget=forms.RadioSelect())
	question_23 = forms.ChoiceField(choices=q23, widget=forms.RadioSelect())
	question_24 = forms.ChoiceField(choices=q24, widget=forms.RadioSelect())
	question_25 = forms.ChoiceField(choices=q25, widget=forms.RadioSelect())
	question_26 = forms.ChoiceField(choices=q26, widget=forms.RadioSelect())
	question_27 = forms.ChoiceField(choices=q27, widget=forms.RadioSelect())
	question_28 = forms.ChoiceField(choices=q28, widget=forms.RadioSelect())
	question_29 = forms.ChoiceField(choices=q29, widget=forms.RadioSelect())


class UserProfileForm(forms.Form):

	OPTION = [
		('Rarely', 'Rarely(Several times a year)'), 
		('Occasionally', 'Occasionally(Several times a month)'),
		('Frequently', 'Frequently(Several times a week)'),
		('Very Frequently', 'Very Frequently(Several times a day)')
		]

	OPTION_GENDER = [
		('Male', 'Male'),
		('Female', 'Female')
		]

	age = forms.CharField()
	gender = forms.ChoiceField(choices=OPTION_GENDER)
	occupation = forms.CharField()
	field_of_study = forms.CharField(label='Field of Study (if student, otherwise enter n/a)')
	simple_bar_chart = forms.ChoiceField(choices=OPTION)
	complex_bar_chart = forms.ChoiceField(choices=OPTION)


