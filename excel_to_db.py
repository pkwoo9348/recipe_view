import openpyxl as xl

dir = r"C:\Users\kp\Desktop\recipe_view\test.xlsx"

# 엑셀 불러오기
excel = xl.load_workbook(dir)

# 시트 선택
excel_ws = excel['테스트']

toDB_url=[]
toDB_data=[]

for i in range(2,excel_ws.max_row):
    toDB_url.append(excel_ws[f'A{i}'].value)
    toDB_data.append(excel_ws[f'B{i}'].value)
excel.close()

toDB_Title=[]
toDB_Ingredients=[]
toDB_Directions=[]

'''
for data in toDB_data:
    open = data.find('[')
    close = data.find(']')
    if open <0:
        continue

    find_title=data[open+1:close]
    
    if find_title.find('재료')>=0:
        continue    

    toDB_Title.append(find_title)
    data=data[close+1:]
    
    close = data.find(']')
    data=data[close+1:]
    open = data.find('[')
    
    toDB_Ingredients.append(data[close+1:open])
    
    data=data[open:]
    close = data.find(']')
    
    data=data[close+1:]
    
    if data.find('자막')>0:
        open = data.find('[')
        toDB_Directions.append(data[:open])
    else:      
        toDB_Directions.append(data)
'''

for data in toDB_data:
    open = data.find('[')
    close = data.find(']')
    if open <0:
        continue

    find_title=data[open+1:close]
    
    if find_title.find('재료')<0:
        continue
    
    open = data.find('=')
    
    data=data[open:].strip('=')

    if open<0:
        continue
    
    open = data.find('[')

    if len(data[:open].strip('\n'))<1:
        continue
    
    toDB_Title.append(data[:open].strip('\n'))
    close=data.find(']')
        
    data=data[close+1:]
    open=data.find('[')
    close = data.find(']')
    toDB_Ingredients.append(data[:open])
    
    data=data[open:]
    close = data.find(']')
    
    data=data[close+1:]
    
    if data.find('자막')>0:
        open = data.find('[')
        toDB_Directions.append(data[:open])
    else:      
        toDB_Directions.append(data)

    
    
    
    
    
print(toDB_Directions[6])
    


