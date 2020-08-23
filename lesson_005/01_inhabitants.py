# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# from room_1 import folks as folks1, __name__ as name1
# from room_2 import folks as folks2, __name__ as name2

# str1 = "В комнате " + name1 + " живут: " + folks1[0] + " и " + folks1[1]
# str2 = "В комнате " + name2 + " живут: " + folks2[0]

import room_1 as r1
import room_2 as r2

str1 = "В комнате " + r1.__name__ + " живут: " + r1.folks[0] + " и " + r1.folks[1]
str2 = "В комнате " + r2.__name__ + " живут: " + r2.folks[0]

print(str1)
print(str2)
