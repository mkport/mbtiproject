import pandas
df = pandas.read_csv('top.csv')

# Receive user inputs for the specified personality types to be used in comparisons
u_mbti=input("Please enter your MBTI type (ex. INTP, or x if not known):")
u_enn=input("Please enter your enneagram (ex. 6w5, or x if not known):")
u_ins=input("Please enter your instinctual variant (ex. sp/so, or x if not known):")
u_tri=str(input("Please enter your tritype (ex. 649, or x if not known):"))
u_soc=input("Please enter your socionics type (ex. SLI, or x if not known):")
u_big=input("Please enter your Big 5 personality type (ex. RCUAI, or x if not known):")
u_att=input("Please enter your attitudinal psyche type (ex. FLEV, or x if not known):")
u_tem=input("Please enter your temperament type (ex. M (Melancholic), MP (Melancholic-Phlegmatic) or x if not known):")
u_jung=input("Please enter your classic Jungian type (ex. IT(N), or x if not known):")

# Create functions for each personality type which return a value that reflects how much the character type matches
# with the user input
# MBTI analysis
def mbti_stats(value):
	if u_mbti == 'x':
		return 0
	elif value == u_mbti:
		return 1
	else:
		count = 0
		a=list(set(value)&set(u_mbti))
		final = 0
		for i in a:
			count += 1
			final = count * 0.25
		return final

# Enneagram analysis
def e_stats(value):
	if u_enn == 'x':
		return 0
	elif value == u_enn:
		return 1
	elif value[0] == u_enn[0]:
		return 0.7
	elif value[0] == u_enn[2] and value[2] == u_enn[0]:
		return 0.5
	elif value[2] == u_enn[2] or value[0] == u_enn[2] or value[2] == u_enn[0]:
		return 0.3
	else:
		return 0

# Instinctual variant analysis
def i_stats(value):
	if u_ins == 'x':
		return 0
	elif value == u_ins:
		return 1
	elif value[1] == u_ins[4] and value[4] == u_ins[1]:
		return 0.75
	elif value[1] == u_ins[1]:
		return 0.66
	elif value[1] == u_ins[4] or value[4] == u_ins[1]:
		return 0.4
	else:
		return 0.3

# Tritype analysis
def tr_stats(value):
	value2=str(value)
	if u_tri == 'x':
		return 0
	elif value == u_tri:
		return 1
	elif len(list(set(value2) & set(u_tri))) == 3:
		return 0.65
	elif value2[0] == u_tri[0]:
		if value2[1] == u_tri[1] or value2[1] == u_tri[2]:
			return 0.75
		elif value2[2] == u_tri[1] or value2[2] == u_tri[2]:
			return 0.75
		else:
			return 0.5
	elif value2[1] == u_tri[0] or value2[2] == u_tri[0]:
		if value2[0] == u_tri[1] or value2[0] == u_tri[2]:
			return 0.4
		elif value2[1] == u_tri[1] or value2[1] == u_tri[2]:
			return 0.5
		elif value2[2] == u_tri[1] or value2[2] == u_tri[2]:
			return 0.5
		else:
			return 0.25
	elif value2[1] == u_tri[1] or value2[1] == u_tri[2] and value2[2] == u_tri[1] or value2[2] == u_tri[2]:
		return 0.5
	elif value2[0] == u_tri[1] or value2[0] == u_tri[2]:
		if value2[1] == u_tri[1] or value2[1] == u_tri[2] or value2[2] == u_tri[1] or value2[2] == u_tri[2]:
			return 0.4
		else:
			return 0.15
	elif value2[1] == u_tri[1] or value2[1] == u_tri[2] or value2[2] == u_tri[1] or value2[2] == u_tri[2]:
		return 0.25
	else:
		return 0

# Socionics analysis
def s_stats(value):
	if u_soc == 'x':
		return 0
	elif value == u_soc:
		return 1
	elif value[0] == u_soc[0]:
		if value[1] == u_soc[1]:
			return 0.7
		elif value[2] == u_soc[2]:
			return 0.65
		else:
			return 0.45
	elif value[1] == u_soc[0]:
		if value[0] == u_soc[1]:
			if value[2] == u_soc[2]:
				return 0.6
			else:
				return 0.45
		else:
			if value[2] == u_soc[2]:
				return 0.45
			else:
				return 0.15
	elif value[2] == u_soc[2]:
		if value[1] == u_soc[1]:
			return 0.65
		elif value[0] == u_soc[1]:
			return 0.45
		else:
			return 0.3
	elif value[0] == u_soc[1]:
		return 0.15
	elif value[1] == u_soc[1]:
		return 0.35
	else:
		return 0

# Big 5 analysis
def b_stats(value):
	if u_big == 'x':
		return 0
	elif value == u_big:
		return 1
	else:
		count = 0
		a=list(set(value)&set(u_big))
		final = 0
		for i in a:
			count += 1
			final = count * 0.2
		return final

# Attitudinal psyche analysis
def a_stats(value):
	if u_att == 'x':
		return 0
	elif value == u_att:
		return 1
	elif value[0] == u_att[0]:
		if value[1] == u_att[1]:
			return 0.9
		elif value[1] == u_att[2]:
			if value[2] == u_att[1]:
				return 0.7
			else:
				return 0.6
		elif value[1] == u_att[3]:
			if value[2] == u_att[1]:
				return 0.55
			else:
				return 0.5
	elif value[0] == u_att[1]:
		if value[1] == u_att[0]:
			if value[2] == u_att[2]:
				return 0.8
			else:
				return 0.7
		elif value[1] == u_att[2]:
			if value[2] == u_att[0]:
				return 0.55
			else:
				return 0.5
		elif value[1] == u_att[3]:
			if value[2] == u_att[0]:
				return 0.45
			else:
				return 0.4
	elif value[0] == u_att[2]:
		if value[1] == u_att[0]:
			if value[2] == u_att[1]:
				return 0.45
			else:
				return 0.4
		elif value[1] == u_att[1]:
			if value[2] == u_att[0]:
				return 0.35
			else:
				return 0.3
		elif value[1] == u_att[3]:
			if value[2] == u_att[0]:
				return 0.15
			else:
				return 0.1
	elif value[0] == u_att[3]:
		if value[1] == u_att[0]:
			if value[2] == u_att[1]:
				return 0.35
			else:
				return 0.3
		elif value[1] == u_att[1]:
			if value[2] == u_att[0]:
				return 0.25
			else:
				return 0.2
		elif value[1] == u_att[2]:
			if value[2] == u_att[0]:
				return 0.05
			else:
				return 0

# Temperament analysis
def te_stats(value):
	if u_tem == 'x':
		return 0
	elif value == u_tem:
		return 1
	elif len(u_tem) == 1:
		if value[0] == u_tem:
			return 0.75
		elif len(value) == 2 and value[1] == u_tem:
			return 0.25
		else:
			return 0
	else:
		if len(value) == 1:
			if value == u_tem[0]:
				return 0.75
			elif value == u_tem[1]:
				return 0.25
			else:
				return 0
		else:
			if value[0] == u_tem[0]:
				return 0.75
			elif value[0] == u_tem[1] and value[1] == u_tem[0]:
				return 0.5
			elif value[1] == u_tem[1]:
				return 0.25
			elif value[0] == u_tem[1] or value[1] == u_tem[0]:
				return 0.4
			else:
				return 0

# Jungian analysis
def j_stats(value):
	if u_jung == 'x' or value == 'x':
		return 0
	elif value == u_jung:
		return 1
	elif value[0] == u_jung[0]:
		if value[1] == u_jung[1]:
			return 0.66
		elif value[3] == u_jung[1]:
			if value[1] == u_jung[3]:
				return 0.91
			else:
				return 0.58
		elif value[1] == u_jung[3]:
			return 0.66
		elif value[3] == u_jung[3]:
			return 0.66
		else:
			return 0.33
	else:
		if value[1] == u_jung[1]:
			if value[3] == u_jung[3]:
				return 0.66
			else:
				return 0.33
		elif value[3] == u_jung[1]:
			if value[1] == u_jung[3]:
				return 0.58
			else:
				return 0.25
		elif value[1] == u_jung[3]:
			return 0.33
		elif value[3] == u_jung[3]:
			return 0.33
		else:
			return 0

# Apply functions to specified columns of df
df['mbti_stats'] = df['MBTI'].map(mbti_stats)
df['e_stats'] = df['Enneagram'].map(e_stats)
df['i_stats'] = df['Instinctual_Variant'].map(i_stats)
df['tr_stats'] = df['Tritype'].map(tr_stats)
df['s_stats'] = df['Socionics'].map(s_stats)
df['b_stats'] = df['Big_5'].map(b_stats)
df['a_stats'] = df['Attitudinal_Psyche'].map(a_stats)
df['te_stats'] = df['Temperament'].map(te_stats)
df['j_stats'] = df['Classic_Jungian'].map(j_stats)

# Find mean from the newly created columns
df["mean"] = df.loc[:, ["mbti_stats", "e_stats", "i_stats", "tr_stats", "s_stats", "b_stats", "a_stats", "te_stats", "j_stats"]].mean(axis = 1)

# Get the top values from the df
df = df.sort_values(by=["mean"], ascending=False)
print(df)

# Option to save results to csv below
# df.to_csv('results.csv')
