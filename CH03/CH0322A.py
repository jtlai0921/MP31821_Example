''' if/else單一條件雙向擇
  2次機會輸入密碼 若輸入值不等於密碼，輸出提示訊息; 若密碼符合則輸出「Welcom Python!!」
'''
saves = 'abc123' #密碼
nums = 2 #儲存輸入密碼次數
pwd = input('你有2次機會，請輸入密碼: ')

# 進入單一條件雙向選擇
if(saves != pwd): #若輸入值不等於密碼
   nums -=1 #扣除次數，nums = nums - 1
   print('你還有', nums, '次機會')
else:
   print('Welcome Python!!') #輸入值等於密碼
