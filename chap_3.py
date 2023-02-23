#list or Arrays?

yugioh_og = ["Dark Magician", "Blue Eyes White Dragon", "Red Eyes Black Dragon", "Exodia", "Slifer the Sky Dragon", "Obelisk the Tormentor", "The Winged Dragon of Ra"]
# yugioh_og[0] = "Time Wizard"

# yugioh_og.append("Dark Magician")
# yugioh_og.append("Toon World ")
# yugioh_og.insert(0, "Wind-up Zenmaines")

# yugioh_og.pop()
# yugioh_og.pop(0)

# yugioh_og.remove("Dark Magician")
# new_message = f'My favorite card is {yugioh_og[0].upper()}'


# print(yugioh_og)
# print(new_message)


#Try it yourself 
guest_list = ["Kobe Bryant", "Michael Jordan", "Lebron James"]

guest_list.remove("Michael Jordan")
guest_list.append("Kareem Abdul-Jabbar")
guest_list.insert(0, "Magic Johnson")
guest_list.insert(3, "Larry Bird")
guest_list.append("Shaquille O'Neal")

# print(f'Hello {guest_list[0]}, I would like to invite you to dinner')
# print(f'Hello {guest_list[1]}, I would like to invite you to dinner')
# print(f'Hello {guest_list[2]}, I would like to invite you to dinner')
# print(f'Hello {guest_list[3]}, I would like to invite you to dinner')
# print(f'Hello {guest_list[4]}, I would like to invite you to dinner')
# print(f'Hello {guest_list[5]}, I would like to invite you to dinner')

# guest_list.sort()                                     # Sorts the list in alphabetical order               
# guest_list.sort(reverse=True)                         # Sorts the list in reverse alphabetical order
# print("Here is the original list: ")
# print(guest_list)
# print ("\n Here is the sorted guest list: ")
# print(sorted(guest_list))                             # Sorts the list in alphabetical order, but does not change the original list

# print("\n Here is the original list again: ")
# print(guest_list)

guest_list.reverse()                                    # Does not sort the list, just reverses the order
print(guest_list)

len(guest_list)                                         # Returns the length of the list
print(len(guest_list))