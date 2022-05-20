# 엑셀 파일 가져오기
# 데이터 가공
# 이상데이터 처리
# db 연동 및 데이터 전송
# db admin/kpadmin12      db: test

import openpyxl as xl
import pymysql
#엑셀 파일 위치
dir = r"C:\Users\kp\Desktop\recipe_view\test.xlsx"

# 엑셀 불러오기
excel = xl.load_workbook(dir)

# 시트 선택
excel_ws = excel['테스트']

toDB_url=[]
toDB_data=[]

# 엑셀 value 리스트에 저장
for i in range(2,excel_ws.max_row):
    toDB_url.append(excel_ws[f'A{i}'].value)
    toDB_data.append(excel_ws[f'B{i}'].value)
excel.close()

toDB_url2=[]
toDB_Title=[]
toDB_Ingredients=[]
toDB_Directions=[]

# 데이터 가공 / 이상값 넘기기
for data in toDB_data:
    i=toDB_data.index(data)
    
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
    
    toDB_url2.append(toDB_url[i])

# 데이터 가공 이상값 처리
for data in toDB_data:
    i=toDB_data.index(data)

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

    toDB_url2.append(toDB_url[i])



# db에 저장
conn = pymysql.connect(host='database-2.clufoxjoavjk.ap-northeast-2.rds.amazonaws.com', user='admin', password='kpadmin12', db='test', charset='utf8')

sql = "INSERT INTO recipe (url, Title, Ingredients, Directions) VALUES (%s, %s,%s, %s)"


with conn:
    with conn.cursor() as cur:
        for i in range(0,len(toDB_url2)):
            cur.execute(sql, (toDB_url2[i], toDB_Title[i], toDB_Ingredients[i], toDB_Directions[i]))
        conn.commit()
        
conn.close()