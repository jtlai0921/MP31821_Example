"""
   replace(old, new[, count])函式
      以new字元替換old字元，若old字元有多個，以count指定次數
      -- old欲替換字元或字串，
      -- new替換字元或字串
      -- count 當old字元有多個時可指定替換次數
"""
print("\n---replace()函式：新字元「週」取代舊字元「星期」---")

work = '星期一，星期二工作天，星期三工作一整天'
print(work)
print(work.replace('星期', '週', 2))
