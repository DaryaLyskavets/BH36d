class Category:
    categories = {}

    @classmethod
    def add(cls, name: str, is_published:bool):
        for key in cls.categories:
            if name not in cls.categories.keys():
                cls.categories.update({name:True})
                return cls.categories
            else:
                raise ValueError

    @classmethod
    def get(cls, key: str):
        return cls.categories.get(name)

    @classmethod
    def delete(cls, key: str)) -> None:
        # if key in range(len(cls.categories():
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