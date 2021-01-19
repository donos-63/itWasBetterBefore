class Garden():

    def _plant(self, legume, quantity):
        if len(self.__garden) > 30:
            raise "No more place"

        self.__garden.add(legume)

    def to_water_all(self, legume, grow):
        for l in self.__garden:
            self.__grow(grow)

    def add_legume(self, legume):
        self._plant(legume)

