import random
#i will write the algorithm as comments in my game.
#this is my function that i will need to shuffle.
#the characters list
list=['a','b','c','d','e','f','g','h','i','j']
newlist=2*list#the list repeated two times
random.shuffle (newlist)#in order to make the list characters randomly
the_numbers_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,5,16,17,18,19,20]#the number list
print("I Hope you enjoy the game lets rock it",the_numbers_list)#print the list that the player will choose from
player1=0#the first player starts
player2=0#the second player starts
while True :
        #setting the list that will a star will appear to the user
  while(the_numbers_list!=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']):
          #playerone turn starts
        print("its your turn go on player one: ")
        #he will choose his two numbers
        number1=int(input("choose a number from the list above: "))
        number2=int(input("choose a second number from the list above: "))
        #in order to replace the old list with the new list without naming another variable
        the_numbers_list[number1-1]=newlist[number1-1]
        the_numbers_list[number2-1]=newlist[number2-1]
        print(the_numbers_list)#printing the new list after it is modified
        if(the_numbers_list[number1-1]==the_numbers_list[number2-1]):
            the_numbers_list[number1-1]=the_numbers_list[number2-1]=newlist[number1-1]=newlist[number2-1]="*"
            player1=player1+1#playing his second try
            print ("player1:",player1,the_numbers_list)
        else:
            the_numbers_list[number1-1]=number1
            the_numbers_list[number2-1]=number2
            print("     player1:   ",player1,the_numbers_list)
            print("    its player 2 turn  ")
            number3=int(input("choose a number from the list above: "))
            number4=int(input("choose a second number from the list above: "))
            the_numbers_list[number3-1]=newlist[number3-1]
            the_numbers_list[number4-1]=newlist[number4-1]
            print(the_numbers_list)
        if(the_numbers_list[number3-1]==the_numbers_list[number4-1]):
            the_numbers_list[number4-1]=the_numbers_list[number3-1]=newlist[number4-1]=newlist[number3-1]='*'
            player2=player2+1
            print ("player2: ",player2,the_numbers_list)
        else:
            the_numbers_list[number3-1]=number3
            the_numbers_list[number4-1]=number4
            print("player2: ",player2,the_numbers_list)
if(player1>player2):
    print("   player one is the winner congratulations  ")
else:
    print("  player two is the winner congratulations   ")
1
