#1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

#Twinkle, twinkle, little star,
#	How I wonder what you are!
#		Up above the world so high,
#		Like a diamond in the sky.
#Twinkle, twinkle, little star,
#	How I wonder what you are


p1='Twinkle, twinkle, little star,\n'
p2='\tHow I wonder what you are!\n'
p3='\t\tUp above the world so high,\n'
p4='\t\tLike a diamond in the sky.\n'
p5='Twinkle, twinkle, little star\n'
p6='\tHow I wonder what you are'
print(p1+p2+p3+p4+p5+p6)