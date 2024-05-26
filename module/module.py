# import price_module
#
# price_module.price(5)
# price_module.moodz_price(4)
# price_module.card_price(3)

# import price_module as pm
#
# pm.price(2)
# pm.moodz_price(4)
# pm.card_price(8)

# from price_module import *
#
# price(2)
# moodz_price(4)
# card_price(2)

from price_module import price, moodz_price

price(2)
moodz_price(4)
# card_price(2) # import 하지 않아서 오류 발생

from price_module import card_price as cp
cp(3)