import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('top.csv')

# The purpose of the next few visualizations is to get a preliminary look at the data
# After these preliminary visualizations, there will be some restructuring using pandas to make the charts and info
# easier to understand
# Preliminary look at MBTI types of dataset
mbti_df = df['MBTI'].value_counts().rename_axis('MBTI').reset_index(name='count')
palette_color = sns.color_palette('colorblind')
plt.pie(mbti_df['count'], labels=mbti_df['MBTI'], colors=palette_color, autopct='%.0f%%')
plt.show()

# Preliminary look at Enneagram types with wing included
enn_df = df['Enneagram'].value_counts().rename_axis('Enneagram').reset_index(name='count')
sns.barplot(data=enn_df, x="Enneagram", y="count")
plt.show()

# Preliminary instinctual variant analysis
iv_df = df['Instinctual_Variant'].value_counts().rename_axis('Instinctual_Variant').reset_index(name='count')
palette_color = sns.color_palette('colorblind')
plt.pie(iv_df['count'], labels=iv_df['Instinctual_Variant'], colors=palette_color, autopct='%.0f%%')
plt.show()

# Preliminary tritype initial analysis
tri_df = df['Tritype'].value_counts().rename_axis('Tritype').reset_index(name='count')
sns.barplot(data=tri_df, x="Tritype", y="count")
plt.show()

# Preliminary socionics initial analysis
soc_df = df['Socionics'].value_counts().rename_axis('Socionics').reset_index(name='count')
sns.barplot(data=soc_df, x="Socionics", y="count")
plt.show()

# Preliminary Big 5 initial analysis
big5_df = df['Big_5'].value_counts().rename_axis('Big_5').reset_index(name='count')
sns.barplot(data=big5_df, x="Big_5", y="count")
plt.show()

# Preliminary attitudinal psyche initial analysis
ap_df = df['Attitudinal_Psyche'].value_counts().rename_axis('Attitudinal_Psyche').reset_index(name='count')
sns.barplot(data=ap_df, x="Attitudinal_Psyche", y="count")
plt.show()

# Preliminary temperament initial analysis
temp_df = df['Temperament'].value_counts().rename_axis('Temperament').reset_index(name='count')
sns.barplot(data=temp_df, x="Temperament", y="count")
plt.show()

# Preliminary classic jungian initial analysis
jung_df = df['Classic_Jungian'].value_counts().rename_axis('Classic_Jungian').reset_index(name='count')
sns.barplot(data=jung_df, x="Classic_Jungian", y="count")
plt.show()

# End of preliminary analysis, time to make the charts easier to understand
# Separate MBTI by dominant, auxiliary, tertiary, and inferior functions
def dominant(value):
    if value == 'ESTP' or value == 'ESFP':
        return 'Se'
    elif value == 'ISTJ' or value == 'ISFJ':
        return 'Si'
    elif value == 'ENTP' or value == 'ENFP':
        return 'Ne'
    elif value == 'INTJ' or value == 'INFJ':
        return 'Ni'
    elif value == 'ESTJ' or value == 'ENTJ':
        return 'Te'
    elif value == 'INTP' or value == 'ISTP':
        return 'Ti'
    elif value == 'ESFJ' or value == 'ENFJ':
        return 'Fe'
    else:
        return 'Fi'

def auxiliary(value):
    if value == 'ISFP' or value == 'ISTP':
        return 'Se'
    elif value == 'ESTJ' or value == 'ESFJ':
        return 'Si'
    elif value == 'INTP' or value == 'INFP':
        return 'Ne'
    elif value == 'ENTJ' or value == 'ENFJ':
        return 'Ni'
    elif value == 'ISTJ' or value == 'INTJ':
        return 'Te'
    elif value == 'ESTP' or value == 'ENTP':
        return 'Ti'
    elif value == 'INFJ' or value == 'ISFJ':
        return 'Fe'
    else:
        return 'Fi'

def tertiary(value):
    if value == 'ENTJ' or value == 'ENFJ':
        return 'Se'
    elif value == 'INTP' or value == 'INFP':
        return 'Si'
    elif value == 'ESTJ' or value == 'ESFJ':
        return 'Ne'
    elif value == 'ISTP' or value == 'ISFP':
        return 'Ni'
    elif value == 'ESFP' or value == 'ENFP':
        return 'Te'
    elif value == 'ISFJ' or value == 'INFJ':
        return 'Ti'
    elif value == 'ENTP' or value == 'ESTP':
        return 'Fe'
    else:
        return 'Fi'

def inferior(value):
    if value == 'ESTP' or value == 'ESFP':
        return 'Ni'
    elif value == 'ISTJ' or value == 'ISFJ':
        return 'Ne'
    elif value == 'ENTP' or value == 'ENFP':
        return 'Si'
    elif value == 'INTJ' or value == 'INFJ':
        return 'Se'
    elif value == 'ESTJ' or value == 'ENTJ':
        return 'Fi'
    elif value == 'INTP' or value == 'ISTP':
        return 'Fe'
    elif value == 'ESFJ' or value == 'ENFJ':
        return 'Ti'
    else:
        return 'Te'

df['dominant'] = df['MBTI'].map(dominant)
df['auxiliary'] = df['MBTI'].map(auxiliary)
df['tertiary'] = df['MBTI'].map(tertiary)
df['inferior'] = df['MBTI'].map(inferior)

dominant_df = df['dominant'].value_counts().rename_axis('function').reset_index(name='count')
auxiliary_df = df['auxiliary'].value_counts().rename_axis('function').reset_index(name='count')
tertiary_df = df['tertiary'].value_counts().rename_axis('function').reset_index(name='count')
inferior_df = df['inferior'].value_counts().rename_axis('function').reset_index(name='count')

figure, axis = plt.subplots(2, 2)

axis[0, 0].pie(dominant_df['count'], labels=dominant_df['function'], colors=palette_color, autopct='%.0f%%')
axis[0, 0].set_title("Dominant Functions")

axis[0, 1].pie(auxiliary_df['count'], labels=auxiliary_df['function'], colors=palette_color, autopct='%.0f%%')
axis[0, 1].set_title("Auxiliary Functions")

axis[1, 0].pie(tertiary_df['count'], labels=tertiary_df['function'], colors=palette_color, autopct='%.0f%%')
axis[1, 0].set_title("Tertiary Functions")

axis[1, 1].pie(inferior_df['count'], labels=inferior_df['function'], colors=palette_color, autopct='%.0f%%')
axis[1, 1].set_title("Inferior Functions")

plt.show()

# Enneagram analysis with Enneagram only and Wing only
def No_Wing(value):
    return value[0]

def Wing_Only(value):
    return value[2]

df['No_Wing'] = df['Enneagram'].map(No_Wing)
no_wing_df = df['No_Wing'].value_counts().rename_axis('Enneagram').reset_index(name='count')

df['Wing_Only'] = df['Enneagram'].map(Wing_Only)
wing_only_df = df['Wing_Only'].value_counts().rename_axis('Enneagram').reset_index(name='count')

figure, axis = plt.subplots(1, 2)

axis[0].pie(no_wing_df['count'], labels=no_wing_df['Enneagram'], colors=palette_color, autopct='%.0f%%')
axis[0].set_title("Enneagram Only")

axis[1].pie(wing_only_df['count'], labels=wing_only_df['Enneagram'], colors=palette_color, autopct='%.0f%%')
axis[1].set_title("Wing Only")

plt.show()

# Instinctual variant analysis with separated primary and secondary variant
def primary_variant(value):
    return value[:2]

def secondary_variant(value):
    return value[-2:]

df['Primary_Variant'] = df['Instinctual_Variant'].map(primary_variant)
primary_variant_df = df['Primary_Variant'].value_counts().rename_axis('Instinctual_Variant').reset_index(name='count')

df['Secondary_Variant'] = df['Instinctual_Variant'].map(secondary_variant)
secondary_variant_df = df['Secondary_Variant'].value_counts().rename_axis('Instinctual_Variant').reset_index(name='count')

figure, axis = plt.subplots(1, 2)

axis[0].pie(primary_variant_df['count'], labels=primary_variant_df['Instinctual_Variant'], colors=palette_color, autopct='%.0f%%')
axis[0].set_title("Primary Instinct")

axis[1].pie(secondary_variant_df['count'], labels=secondary_variant_df['Instinctual_Variant'], colors=palette_color, autopct='%.0f%%')
axis[1].set_title("Secondary Instinct")

plt.show()

# Tritype analysis which brings together the counts of each Enneagram type from the tritype
# Ex: Tritype 738 will bring one count to Enneagram types 7, 3, 8
def one_tri(value):
    new = str(value)
    return new[0]

def two_tri(value):
    new = str(value)
    return new[1]

def three_tri(value):
    new = str(value)
    return new[2]

df['one_tri'] = df['Tritype'].map(one_tri)
df['two_tri'] = df['Tritype'].map(two_tri)
df['three_tri'] = df['Tritype'].map(three_tri)
one_tri_df = df['one_tri'].value_counts().rename_axis('Enneagram').reset_index(name='count')
two_tri_df = df['two_tri'].value_counts().rename_axis('Enneagram').reset_index(name='count')
three_tri_df = df['three_tri'].value_counts().rename_axis('Enneagram').reset_index(name='count')
df_temp = pd.concat([one_tri_df, two_tri_df, three_tri_df], axis=0)

agg_func = {'count': 'sum'}
tritype_df = df_temp.groupby(df_temp['Enneagram']).aggregate(agg_func)
tritype_df['Enneagram'] = tritype_df.index
sns.barplot(data=tritype_df, x="Enneagram", y="count")
plt.show()

# Socionics analysis separating the type by letter
def one_soc(value):
    return value[0]

def two_soc(value):
    return value[1]

def three_soc(value):
    return value[2]

df['one_soc'] = df['Socionics'].map(one_tri)
df['two_soc'] = df['Socionics'].map(two_tri)
df['three_soc'] = df['Socionics'].map(three_tri)
one_soc_df = df['one_soc'].value_counts().rename_axis('Letter').reset_index(name='count')
two_soc_df = df['two_soc'].value_counts().rename_axis('Letter').reset_index(name='count')
three_soc_df = df['three_soc'].value_counts().rename_axis('Letter').reset_index(name='count')

figure, axis = plt.subplots(1, 3)

axis[0].pie(one_soc_df['count'], labels=one_soc_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[0].set_title("First Letter")

axis[1].pie(two_soc_df['count'], labels=two_soc_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[1].set_title("Second Letter")

axis[2].pie(three_soc_df['count'], labels=three_soc_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[2].set_title("Third Letter")

plt.show()

# Big 5 analysis separating the type by letter
def first_big5(value):
    return value[0]

def second_big5(value):
    return value[1]

def third_big5(value):
    return value[2]

def fourth_big5(value):
    return value[3]

def fifth_big5(value):
    return value[4]

df['first_big5'] = df['Big_5'].map(first_big5)
df['second_big5'] = df['Big_5'].map(second_big5)
df['third_big5'] = df['Big_5'].map(third_big5)
df['fourth_big5'] = df['Big_5'].map(fourth_big5)
df['fifth_big5'] = df['Big_5'].map(fifth_big5)

first_big5_df = df['first_big5'].value_counts().rename_axis('Letter').reset_index(name='count')
second_big5_df = df['second_big5'].value_counts().rename_axis('Letter').reset_index(name='count')
third_big5_df = df['third_big5'].value_counts().rename_axis('Letter').reset_index(name='count')
fourth_big5_df = df['fourth_big5'].value_counts().rename_axis('Letter').reset_index(name='count')
fifth_big5_df = df['fifth_big5'].value_counts().rename_axis('Letter').reset_index(name='count')

figure, axis = plt.subplots(2, 3)
figure.delaxes(ax=axis[1, 2])

axis[0, 0].pie(first_big5_df['count'], labels=first_big5_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[0, 0].set_title("Extroversion")

axis[0, 1].pie(second_big5_df['count'], labels=second_big5_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[0, 1].set_title("Neuroticism")

axis[0, 2].pie(third_big5_df['count'], labels=third_big5_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[0, 2].set_title("Conscientiousness")

axis[1, 0].pie(fourth_big5_df['count'], labels=fourth_big5_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[1, 0].set_title("Agreeableness")

axis[1, 1].pie(fifth_big5_df['count'], labels=fifth_big5_df['Letter'], colors=palette_color, autopct='%.0f%%')
axis[1, 1].set_title("Openness")

plt.show()

# Attitudinal psyche analysis with separated confident, flexible, insecure, and unbothered values
def confident(value):
    return value[0]

def flexible(value):
    return value[1]

def insecure(value):
    return value[2]

def unbothered(value):
    return value[3]

df['confident'] = df['Attitudinal_Psyche'].map(confident)
df['flexible'] = df['Attitudinal_Psyche'].map(flexible)
df['insecure'] = df['Attitudinal_Psyche'].map(insecure)
df['unbothered'] = df['Attitudinal_Psyche'].map(unbothered)

confident_df = df['confident'].value_counts().rename_axis('function').reset_index(name='count')
flexible_df = df['flexible'].value_counts().rename_axis('function').reset_index(name='count')
insecure_df = df['insecure'].value_counts().rename_axis('function').reset_index(name='count')
unbothered_df = df['unbothered'].value_counts().rename_axis('function').reset_index(name='count')

figure, axis = plt.subplots(2, 2)

axis[0, 0].pie(confident_df['count'], labels=confident_df['function'], colors=palette_color, autopct='%.0f%%')
axis[0, 0].set_title("Confident Functions")

axis[0, 1].pie(flexible_df['count'], labels=flexible_df['function'], colors=palette_color, autopct='%.0f%%')
axis[0, 1].set_title("Flexible Functions")

axis[1, 0].pie(insecure_df['count'], labels=insecure_df['function'], colors=palette_color, autopct='%.0f%%')
axis[1, 0].set_title("Insecure Functions")

axis[1, 1].pie(unbothered_df['count'], labels=unbothered_df['function'], colors=palette_color, autopct='%.0f%%')
axis[1, 1].set_title("Unbothered Functions")

plt.show()

# Temperament analysis separating the first and second temperaments (if they are not dominant)
def first_temp(value):
    return value[0]

def second_temp(value):
    if len(value) == 1:
        return value[0]
    else:
        return value[1]

df['first_temp'] = df['Temperament'].map(first_temp)
df['second_temp'] = df['Temperament'].map(second_temp)

first_temp_df = df['first_temp'].value_counts().rename_axis('Type').reset_index(name='count')
second_temp_df = df['second_temp'].value_counts().rename_axis('Type').reset_index(name='count')

figure, axis = plt.subplots(1, 2)

axis[0].pie(first_temp_df['count'], labels=first_temp_df['Type'], colors=palette_color, autopct='%.0f%%')
axis[0].set_title("First Type")

axis[1].pie(second_temp_df['count'], labels=second_temp_df['Type'], colors=palette_color, autopct='%.0f%%')
axis[1].set_title("Second Type")

plt.show()

# Jungian analysis separated by letter
def primary_jungian(value):
    return value[:2]

def secondary_jungian(value):
    return value[3]

df['Primary_Jungian'] = df['Classic_Jungian'].map(primary_jungian)
df['Secondary_Jungian'] = df['Classic_Jungian'].map(secondary_jungian)
primary_jungian_df = df['Primary_Jungian'].value_counts().rename_axis('Function').reset_index(name='count')
secondary_jungian_df = df['Secondary_Jungian'].value_counts().rename_axis('Function').reset_index(name='count')

figure, axis = plt.subplots(1, 2)

axis[0].pie(primary_jungian_df['count'], labels=primary_jungian_df['Function'], colors=palette_color, autopct='%.0f%%')
axis[0].set_title("Primary Jungian")

axis[1].pie(secondary_jungian_df['count'], labels=secondary_jungian_df['Function'], colors=palette_color, autopct='%.0f%%')
axis[1].set_title("Secondary Jungian")

plt.show()
