# ____1 задание_____

# class PastaBuilder:
#     def __init__(self):
#         self._type = None
#         self._sauce = None
#         self._filling = None
#         self._toppings = []
#
#     def set_type(self, pasta_type):
#         self._type = pasta_type
#         return self
#
#     def set_sauce(self, sauce):
#         self._sauce = sauce
#         return self
#
#     def set_filling(self, filling):
#         self._filling = filling
#         return self
#
#     def add_topping(self, topping):
#         self._toppings.append(topping)
#         return self
#
#     def build(self):
#         return Pasta(self._type, self._sauce, self._filling, self._toppings)
#
#
# class Pasta:
#     def __init__(self, pasta_type, sauce, filling, toppings):
#         self.pasta_type = pasta_type
#         self.sauce = sauce
#         self.filling = filling
#         self.toppings = toppings
#
#
#     def __str__(self):
#         return (f"Паста: {self.pasta_typen}"
#             f"Соус: {self.saucen}"
#             f"Начинка: {self.fillingn}"
#             f"Добавки: {', '.join(self.toppings)}")
#
#
#     def main():
#         spaghetti_builder = (PastaBuilder()
#                          .set_type("Спагетти")
#                          .set_sauce("Томатный соус")
#                          .set_filling("Фарш из говядины")
#                          .add_topping("Тёртый сыр")
#                          .add_topping("Базилик"))
#
#         penne_builder = (PastaBuilder()
#                      .set_type("Пене")
#                      .set_sauce("Альфредо")
#                      .set_filling("Курица")
#                      .add_topping("Парма")
#                      .add_topping("Перец"))
#
#         lasagna_builder = (PastaBuilder()
#                        .set_type("Лазанья")
#                        .set_sauce("Бешамель и томатный соус")
#                        .set_filling("Рикотта, шпинат")
#                        .add_topping("Моцарелла")
#                        .add_topping("Пармезан"))
#
#         spaghetti = spaghetti_builder.build()
#         penne = penne_builder.build()
#         lasagna = lasagna_builder.build()
#
#         print(spaghetti)
#         print()
#         print(penne)
#         print()
#         print(lasagna)
#
#     if __name__ == "__main__":
#         main()



# ____2 задание_____
#
# from abc import ABC, abstractmethod
#
# class Pasta(ABC):
#
#     def __init__(self):
#         self._type = None
#         self._sauce = None
#         self._toppings = []
#         self._additives = []
#
#     @abstractmethod
#     def prepare(self):
#         pass
#
#     def set_type(self, pasta_type):
#         self._type = pasta_type
#
#     def set_sauce(self, sauce):
#         self._sauce = sauce
#
#     def add_topping(self, topping):
#         self._toppings.append(topping)
#
#     def add_additive(self, additive):
#         self._additives.append(additive)
#
#     @property
#     def __str__(self):
#         return f"Паста: {self._typenСоус: {self._saucenНачинка: {', '.join(self._toppings)}nДобавки: {', '.join(self._additives)}"
#
# class Spaghetti(Pasta):
#     def prepare(self):
#         self.set_type("Спагетти")
#
# class Penne(Pasta):
#     def prepare(self):
#         self.set_type("Пене")
#
# class Fettuccine(Pasta):
#     def prepare(self):
#         self.set_type("Феттуччине")
#
#
# class PastaBuilder:
#     def __init__(self):
#         self.pasta = None
#
#     def create_new_pasta(self, pasta_type):
#         if pasta_type == "Спагетти":
#             self.pasta = Spaghetti()
#         elif pasta_type == "Пене":
#             self.pasta = Penne()
#         elif pasta_type == "Феттуччине":
#             self.pasta = Fettuccine()
#         else:
#             raise ValueError("Неизвестный тип пасты")
#         self.pasta.prepare()
#
#     def build_sauce(self, sauce):
#         self.pasta.set_sauce(sauce)
#
#     def build_topping(self, toppings):
#         for topping in toppings:
#             self.pasta.add_topping(topping)
#
#     def build_additive(self, additives):
#         for additive in additives:
#             self.pasta.add_additive(additive)
#
#     def get_pasta(self):
#         return self.pasta
#
# class PastaDirector:
#     def __init__(self, builder):
#         self.builder = builder
#
#     def make_pasta(self, pasta_type, sauce, toppings, additives):
#         self.builder.create_new_pasta(pasta_type)
#         self.builder.build_sauce(sauce)
#         self.builder.build_topping(toppings)
#         self.builder.build_additive(additives)
#         return self.builder.get_pasta()
#
#
# if __name__ == "__main__":
#
#     builder = PastaBuilder()
#     director = PastaDirector(builder)
#
#
#     pasta = director.make_pasta("Спагетти", "Томатный соус", ["Фрикадельки"], ["Сыр"])
#     print(pasta)
#     print()
#     pasta = director.make_pasta("Пене", "Альфредо", ["Курица"], ["Зелень"])
#     print(pasta)
#     print()
#     pasta = director.make_pasta("Феттуччине", "Песто", ["Креветки"], ["Чеснок"])
#     print(pasta)


# ____3 задание_____
#
#
# import copy
#
#
# class Pasta:
#     def __init__(self, pasta_type, sauce, filling, toppings=None):
#         self.pasta_type = pasta_type
#         self.sauce = sauce
#         self.filling = filling
#         self.toppings = toppings if toppings is not None else []
#
#     def clone(self):
#         return copy.deepcopy(self)
#
#     def __str__(self):
#         return (f"Паста: {self.pasta_typen}"
#                 f"Соус: {self.saucen}"
#                 f"Начинка: {self.fillingn}"
#                 f"Добавки: {', '.join(self.toppings)}")
#
#
#
# def main():
#
#     original_spaghetti = Pasta(
#         pasta_type="Спагетти",
#         sauce="Томатный соус",
#         filling="Фарш из говядины",
#         toppings=["Тёртый сыр", "Базилик"]
#     )
#
#
#     cloned_spaghetti = original_spaghetti.clone()
#     cloned_spaghetti.sauce = "Песто"
#     cloned_spaghetti.toppings.append("Оливки")
#
#
#     print("Оригинальная паста:")
#     print(original_spaghetti)
#     print()
#     print("Клонированная паста:")
#     print(cloned_spaghetti)
#
# if __name__ == "__main__":
#     main()
#






