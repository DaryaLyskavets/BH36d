class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        for i in cls.categories:
            if name not in cls.categories:
                cls.categories.append(name)
                return cls.categories.index(name)
            else:
                raise ValueError

    @classmethod
    def get(cls, index: int):
        return cls.categories[index]

    @classmethod
    def delete(cls, index: int) -> None:
        # if index in range(len(cls.categories():
        #     del cls.categories[index]
        try:
            del cls.categories[index]
        except IndexError:
            pass

    @classmethod
    def update(cls,index: int, new_name: str):
        if index not in range(len(cls.categories())):
            cls.add(new_name)
        elif new_name not in cls.categories:
            cls.categories[index] = new_name
        else:
            raise ValueError