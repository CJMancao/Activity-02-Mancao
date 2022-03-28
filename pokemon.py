import random

#Determine the effectiveness of the attack
def attack_types(attack, defense):

    inefective = 0

    nve = [.25, .5]
    not_Very_Effective = random.choice(nve)
    
    normal = 1

    super_Effective = 2

    if attack == "fire"  and defense == "water":
        print("\nNot very effective!")
        return not_Very_Effective
    if attack == "fire" and defense == "fire":
        return normal
    if attack == "fire" and defense == "grass":
        print("\nSuper effective!")
        return super_Effective

    if attack == "water"  and defense == "grass":
        print("\nNot very effective!")
        return not_Very_Effective
    if attack == "water" and defense == "water":
        return normal
    if attack == "water" and defense == "fire":
        print("\nSuper effective!")
        return super_Effective

    if attack == "grass"  and defense == "fire":
        print("\nNot very effective!")
        return not_Very_Effective
    if attack == "grass" and defense == "grass":
        return normal
    if attack == "grass" and defense == "water":
        print("\nSuper effective!")
        return super_Effective
    
#Modifier formula
def modifier(target,weather):

    #Target count
    if target >=2:          
        target = 0.5
    if target == 1:
        target = 1

    #Weather
    if weather == "beneficial":
        weather = 1.5
    if weather  == "againts":
        weather = 0.5
    if weather == "normal":
        weather = 1

    #Critical random
    crit= [1 ,2 , 4]
    critic = random.choice(crit)
    if critic >= 2 and attack_types(atkType,dfsType) >=2:
        print("\nA Critical Hit!\n")
    #random
    r = [0.85, 1]
    rand = random.choice(r) 


    modi = target * weather * attack_types(atkType,dfsType) * critic * rand
    return  modi
   
#Calculate the damage of the attacker
def calculate_damage(level,atk,dfs,pow):
    return (((2*level/5)+2) * pow * atk / dfs) / 50 + 2

#---------------------Choose 1st Pokemon-----------------#
print("\nWho is the attacker?")
firstPokemon = int(input("\n1.Charizard \n2.Feraligatr \n3.Venusaur\nChoose your pokemon(1-3):"))

#Charizard
if firstPokemon == 1:
    firstPokemon = "Charizard"
    print("\nYou chose Charizard\n")
    atkType = "fire"
    move = int(input("1.Fire Blast(110 power) \n2.slash(70 power) \n\nChoose your move!:"))
    if move == 1:
        pow = 110
        stab = 1.5
        move = "Fire Blast and gains same type attack bonus"
    if move == 2:
        pow = 70
        stab = 1
        move = "Slash"
    level = int(input("Level:"))
    atk = int(input("attack:"))

#Feraligatr
if firstPokemon == 2:
    firstPokemon = "Feraligatr"
    print("\nYou chose Feraligatr\n")
    atkType = "water"
    move = int(input("1.Hydropump(110 power) \n2.Thrash(120 power)\n\nChoose your move!:"))
    if move == 1:
        pow = 110
        stab = 1.5
        move = "Hydropump and gains same type-attack bonus "
    if move == 2:
        pow = 120
        stab = 1
        move = "Thrash"
    level = int(input("Level:"))
    atk = int(input("attack:"))

#Venusaur
if firstPokemon == 3:
    firstPokemon = "Venusaur"
    print("\nYou chose Venusaur\n")
    atkType = "grass"
    move = int(input("1.Solar beam(120 power) \n2.double edge(120 power)\n\nChoose your move!:"))
    if move == 1:
        pow = 120
        stab = 1.5
        move = "Solar beam and gains same type-attack bonus"
    if move == 2:
        pow = 120
        stab = 1
        move = "Double edge"
    level = int(input("Level:"))
    atk = int(input("attack:"))

#---------------------Choose 2nd Pokemon-----------------#
print("\nWho is defending?")
secondPokemon= int(input("\n1.Charizard \n2.Feraligatr \n3.Venusaur\nChoose your pokemon(1-3):"))

#Charizard
if secondPokemon == 1:
    secondPokemon = "Charizard"
    print("\nYou chose Charizard\n")
    dfsType = "fire"
    level = int(input("Level:"))
    dfs = int(input("defense:"))

#Feraligatr
if secondPokemon == 2:
    secondPokemon = "Feraligatr"
    print("\nYou chose Feraligatr\n")
    dfsType = "water"
    level = int(input("Level:"))
    dfs = int(input("defense:"))

#Venusaur
if secondPokemon == 3:
    secondPokemon = "Venausar"
    print("\nYou chose Venusaur\n")
    dfsType = "grass"
    level = int(input("Level:")) 
    dfs = int(input("defense:"))

target = int(input("\ntarget:"))
print("\nChoose:beneficial, againts,normal")
weather = input("weather:")

#Calculate the total damage of the attacker
calculate = calculate_damage(level,atk,dfs,pow) * modifier(target,weather) * stab

print("\n{}{}{}{}{}{}{}{}".format (firstPokemon , " Attacks " , secondPokemon , " using " , move ," and deals ", calculate , " damage"))