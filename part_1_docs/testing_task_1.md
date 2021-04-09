### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  # The if statement needs a double equals '=='
  # The else statement needs a colon 'else:'
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   

  # Should be 'def', not 'dif. 
  # Also need a comma between card1 and card2, 'card1, card2'
  # 'return card' will fail. Should be 'return card1'
  # The if, else, and both return statments all need indented by one, to be nested under the function definition.
  dif highest_card(self, card1 card2): 
  if card1.value > card2.value:
    return card 
  else:
    return card2
  
# The function is sitting outside of the class. Everything needs indented by 1
# initla 'total' value is undefined right now. Should be 'total = 0' 
# return needs unindented by 1. Currently, the loop will stop after one 'card' iteration
# return string + total will not work
# Could use a formatted string to make it work, e.g. return f"You have a total of {total}"
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
     
  
```
