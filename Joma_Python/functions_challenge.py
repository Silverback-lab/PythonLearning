def score(total, correct, wrong):
    correct_score = 2 * min(total * 0.75, correct)
    wrong_score = 1 * min(max(total * 0.75 - correct,0), wrong)
    perfect_score = 2 * total * 0.75
    return (correct_score + wrong_score)/perfect_score * 100


print (score(20,20,0))
print (score(20,15,0))
print (score(20,15,5))
print (score(20,10,5))
print (score(20,0,20))


#Answer With No Variables
'''
def score_no_variables(total, correct, wrong):
    ((2 * min(total * 0.75, correct)) + (1 * min(max(total * 0.75 - correct,0), wrong)))/(2 * total * 0.75) * 100
'''