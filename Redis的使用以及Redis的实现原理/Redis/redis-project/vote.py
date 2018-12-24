import time

ONE_WEEK_IN_SECONDS = 7*86400
VOTE_SCORE = 432

def article_vote(conn,user,article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

print "123"