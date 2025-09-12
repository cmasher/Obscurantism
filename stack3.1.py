request_str = "Введите пожадуйста"
animal_str =  "питомца:"
print(request_str, "вид", animal_str ,sep=' ')
species = input()
print(request_str, "возраст", animal_str, 
     "пример ввода: \"34 года\", \"12 лет\", я за вас возраст склонять не буду", sep=' ')
age = input()
print(request_str, "кличку", animal_str ,sep=' ')
name = input()

species_preset = "Это " + species 
name_preset = " по кличке " + "\"" + name + "\"" +"."
age_preset = " Возраст: " + age
print(species_preset, name_preset, age_preset, sep='')