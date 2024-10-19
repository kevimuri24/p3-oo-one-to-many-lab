class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self._name = None
        self._pet_type = None
        self._owner = None
        
        self.name = name
        self.pet_type = pet_type
        
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            self.owner = owner
            owner.add_pet(self)
            
        Pet.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if not isinstance(value, str):
            raise Exception("Pet type must be a string.")
        if value.lower() not in Pet.PET_TYPES:
            raise Exception("Invalid pet type. Must be one of: " + ", ".join(Pet.PET_TYPES))
        self._pet_type = value.lower()
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self._owner = value

class Owner:
    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value
    
    def pets(self):
        """Returns a list of all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Adds a pet to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet Class")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Returns a sorted list of pets by name"""
        return sorted(self.pets(), key=lambda x: x.name)
