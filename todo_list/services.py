import random
import string

from rest_framework.response import Response

from todo_list.models import TodoList


class GenerateUUID:

    def __init__(self, cyrillic: bool, length: int):
        self.letters = string.ascii_lowercase + string.ascii_uppercase + \
                       string.digits
        if cyrillic:
            cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
            self.letters += cyrillic_letters

        self.length = length

    def create_uuid(self):
        while True:
            new_uuid = ''.join(random.choice(self.letters) for i in range(self.length))

            exist = TodoList.objects.filter(uuid=new_uuid)
            if not exist:
                return new_uuid



def get_data_response(serializer, items, many=True, check_valid=False, status=200):
    if not items:
        return Response([])

    items_serializer = serializer(items, many=many)

    if check_valid:
        items_serializer.is_valid(raise_exception=True)

    return Response(data=items_serializer.data, status=status)