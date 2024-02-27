class Character():

  def __init__(self, char_name, char_description):
     self.name = char_name
     self.description = char_description
     self.conversation = None

# Describe this character
def describe(self):
    print( self.name + " is here!" )
    print( self.description )

 # Set what this character will say when talked to
def set_conversation(self, conversation):
     self.conversation = conversation

# Talk to this character
def talk(self):
  if self.conversation is not None:
    print("[" + self.name + " says]: " + self.conversation)
  else:
    print(self.name + " doesn't want to talk to you")

# Fight with this character
def fight(self, combat_item):
    print(self.name + " doesn't want to fight with you")
    return True

#Now im going to define Dave
Dave = Character('Dave', 'Dave is a friendly guy who works at the local coffee shop')
describe(Dave)
set_conversation(Dave, 'Hey there! How are you doing today?')
print('\n')
talk(Dave)
\



class Enemy(Character):
 def __init__(self, char_name, char_description):
  super().__init__(char_name, char_description)


class Enemy(Character):
     def __init__(self, char_name, char_description):
       super().__init__(char_name, char_description)
       self.weakness = None


def set_weakness(self, item_weakness):
     self.weakness = item_weakness

     def get_weakness(self):
        return self.weakness

def fight(self, combat_item):
      if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
      else:
         print(self.name + " crushes you, puny adventurer")
      return False

print("What will you fight with?")
fight_with = input()

Dave.fight(fight_with)


