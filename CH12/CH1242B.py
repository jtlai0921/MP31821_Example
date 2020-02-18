#dump()須有參數fp
import json
from io import StringIO

data = {'C':'Three', 'B':'Two', 'D':'Four'}

floi = StringIO()#寫入

json.dump(['A = One'], floi)
data_json = json.dump(data, floi, sort_keys = True)
print(floi.getvalue())#輸出內容
