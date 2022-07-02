import string


def can_repit(n: int):
    def repit(c: string):
        return c * n
    return repit


repit_2 = can_repit(3)
print(repit_2('string'))
