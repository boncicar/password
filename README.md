# 第1版本為while True，當輸入正確密碼時，印出'登入成功'。當輸入不正確密碼時，印出'密碼錯誤! 還有__次機會'
# 第2版本為while True，當輸入正確密碼時，印出'登入成功'。當輸入不正確密碼時，印出'密碼錯誤! 還有2次機會'-->無法遞減(因為remaining = 3在while迴圈內)
# 第3版本為while True(且remaining = 3移到while迴圈外)。當輸入正確密碼時，印出'登入成功'。當輸入不正確密碼時，印出'密碼錯誤! 還有2次機會'-->可遞減。當輸入第3次不正確密碼時，印出'密碼錯誤! 還有0次機會'(因為最後加上if remaining == 0: 跳出迴圈，如果沒加上此程式碼，當再繼續輸入不正確密碼後會印出'密碼錯誤! 還有-1-->-2-->-3...次機會')
# 第4版本將while True改成 while remaining > 0。表示當 remaining大於0才可重複迴圈，與while True一直可重複迴圈不同。else後改寫的目的是要將'還有0次機會'去掉。當輸入第3次不正確密碼後只會印出'密碼錯誤'。
# 第5版本在while回圈內加入elif跟else，表示如果remaining > 0時會印出'密碼錯誤! 還有~次機會'，否則印出'密罵錯誤! 已無法登入!'所以當輸入第3次不正確密碼時，因remaining已經為0，所以印出'密碼錯誤! 已無法登入!'。
# 第6版本在最後加上break，讓輸入第3次不正確密碼後印出'密碼錯誤! 已無法登入!'並終止程式。
# remaining表示輸入密碼次數: remaining = 3表示最多輸入3次機會。