def word_lists(x):
    if x == "animals": 
        word_animal = ["dog","cow","cat","horse","donkey","tiger","lion","panther",
                       "leopard","cheetah","bear","elephant","turtle","tortoise","crocodile",
                       "rabbit","porcupine","hare","hen","pigeon","albatross","crow","fish",
                       "dolphin","frog","whale","alligator","eagle","ostrich","fox",
                       "goat","jackal","emu","armadillo","eel","goose","wolf",
                       "beagle","gorilla","chimpanzee","monkey","beaver","orangutan","antelope","bat",
                       "badger","giraffe","panda","hamster","cobra","camel","hawk","deer","chameleon",
                       "hippopotamus","jaguar","chihuahua","cobra","ibex",
                       "lizard","koala","kangaroo","iguana","llama","chinchillas","dodo","jellyfish",
                       "rhinoceros","hedgehog","zebra","possum","wombat","bison","bull","buffalo",
                       "sheep","meerkat","mouse","otter","sloth","owl","vulture","flamingo",
                       "racoon","mole","duck","swan","lynx","lizard","elk","boar",
                       "lemur","mule","baboon","mammoth","whale","rat","snake","peacock"]
        return word_animal 
    elif x == "cars":
        word_cars = ["ford", "volvo", "opel", "suzuki", "nissan", "kia", "toyota", "mazda",
                     "citroen", "ferrari", "honda", "dodge", "rover", "audi", "mini",
                     "porsche", "tesla", "hyundai", "bmw", "chrysler"]
        return word_cars
    elif x == "cities":
        word_cities = ["stockholm", "paris", "rom", "tokyo", "malmö", "linköping", "norrköping", "oslo",
                       "london", "belfast", "bangladesh", "edinburg", "glasgow", "tianjin"]
        return word_cities
    elif x == "body":
        word_body = ["arm", "leg", "femur", "skull", "thorso", "neck", "foot", "hand", "eyes", "fingers",
                     "toes", "mouth", "cheak", "belly", "palm", "breasts"]
        return word_body