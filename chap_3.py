#list or Arrays?

yugioh_og = ["Dark Magician", "Blue Eyes White Dragon", "Red Eyes Black Dragon", "Exodia", "Slifer the Sky Dragon", "Obelisk the Tormentor", "The Winged Dragon of Ra"]
yugioh_og[0] = "Time Wizard"

yugioh_og.append("Dark Magician")
yugioh_og.append("Toon World ")
yugioh_og.insert(0, "Wind-up Zenmaines")
new_message = f'My favorite card is {yugioh_og[0].upper()}'


print(yugioh_og)
print(new_message)