from sys import argv

script, Kenneth = argv
prompt = ' > '

print "Hi %s, I'm the %s script." % (Kenneth, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % Kenneth
likes = raw_input(prompt)

print "Where do you live %s?" % Kenneth 
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not usre where that is.
And you have a %r computer. NIce
""" % (likes, lives, computer)
