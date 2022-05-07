# DATA MEASURED & CALCULATED EXTERNALLY
# x0 = 138p
# y0 = 452p
# card_x = 298
# card_y = 452
# thanks to the above, I can calculate pixel coordinates of all 4 card corners
# blank_x = 62
# blank_y = 66
# the last two params can help me calculate the next card offset, both X and Y (which means row and column)

from PIL import Image

deck_image = Image.open("full_deck.png")
# deck_image.show()

delta_x = 68 + 298
delta_y = 65 + 452

symbols = {
    0: "_of_clubs",
    1: "_of_spades",
    2: "_of_hearts",
    3: "_of_diamonds",
}

for row in range(4):
    for col in range(14):
        height = 583 + row * delta_y
        y_p = 131 + row * delta_y

        if col == 1:
            x_p = 130 + col * delta_x
            width = 430 + col * delta_x
        else:
            x_p = 136 + col * delta_x
            width = 436 + col * delta_x

        params = (x_p, y_p, width, height)

        cropped = deck_image.crop(params)
        # cropped = cropped_before.resize((55, 83))
        # cropped.show()

        if col == 0 or col == 10 or col == 11 or col == 12 or col == 13:

            if col == 0:
                name = "joker"
            elif col == 10:
                name = "jack"
            elif col == 11:
                name = "queen"
            elif col == 12:
                name = "king"
            elif col == 13:
                name = "ace"

            cropped.save(f"{name}{symbols[row]}.png")

        else:
            cropped.save(f"{col+1}{symbols[row]}.png")

