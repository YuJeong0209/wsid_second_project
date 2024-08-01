# import pandas as pd
# import mysql.connector

# # CSV 파일 읽기
# file_path = 'HW_LDGS_FCLTY_INFO_202306.csv'  # 경로를 올바르게 설정해주세요.
# data = pd.read_csv(file_path)

# # MySQL 데이터베이스 연결 설정
# db_config = {
#     'user': 'your_username',        # MySQL 사용자 이름
#     'password': 'your_password',    # MySQL 비밀번호
#     'host': 'your_host',            # MySQL 호스트 (예: 'localhost')
#     'database': 'your_database'     # 사용할 데이터베이스 이름
# }

# # MySQL 데이터베이스에 연결
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# # 테이블 생성 쿼리
# create_table_query = """
# CREATE TABLE IF NOT EXISTS HW_LDGS_FCLTY_INFO (
#     LDGS_NM VARCHAR(200),
#     CTPRVN_NM VARCHAR(200),
#     GUGUN_NM VARCHAR(200),
#     CFR_LDGS_LIST_CN VARCHAR(1000),
#     ONE_QUARTER_AVRG_PRC DECIMAL(28, 5),
#     TWO_QUARTER_AVRG_PRC DECIMAL(28, 5),
#     GSRM_CO DECIMAL(38, 0),
#     PRKPLCE_EXST_AT VARCHAR(1),
#     RSTRNT_EXST_AT VARCHAR(1),
#     BAR_AT VARCHAR(1),
#     CAFE_HOLD_AT VARCHAR(1),
#     FITNES_CNTER_AT VARCHAR(1),
#     OUTDOOR_POOL_AT VARCHAR(1),
#     SPA_AT VARCHAR(1),
#     SAUNA_AT VARCHAR(1),
#     BNQTHL_AT VARCHAR(1),
#     BSINES_CNTER_AT VARCHAR(1),
#     BEACH_AT VARCHAR(1)
# );
# """
# cursor.execute(create_table_query)

# # 데이터 삽입 쿼리
# insert_query = """
# INSERT INTO HW_LDGS_FCLTY_INFO (
#     LDGS_NM, CTPRVN_NM, GUGUN_NM, CFR_LDGS_LIST_CN, ONE_QUARTER_AVRG_PRC, 
#     TWO_QUARTER_AVRG_PRC, GSRM_CO, PRKPLCE_EXST_AT, RSTRNT_EXST_AT, BAR_AT, 
#     CAFE_HOLD_AT, FITNES_CNTER_AT, OUTDOOR_POOL_AT, SPA_AT, SAUNA_AT, 
#     BNQTHL_AT, BSINES_CNTER_AT, BEACH_AT
# ) VALUES (
#     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
#     %s, %s, %s, %s, %s, %s, %s, %s
# );
# """

# # 데이터 삽입
# for index, row in data.iterrows():
#     cursor.execute(insert_query, (
#         row['LDGS_NM'], row['CTPRVN_NM'], row['GUGUN_NM'], row['CFR_LDGS_LIST_CN'], row['ONE_QUARTER_AVRG_PRC'], 
#         row['TWO_QUARTER_AVRG_PRC'], row['GSRM_CO'], row['PRKPLCE_EXST_AT'], row['RSTRNT_EXST_AT'], row['BAR_AT'], 
#         row['CAFE_HOLD_AT'], row['FITNES_CNTER_AT'], row['OUTDOOR_POOL_AT'], row['SPA_AT'], row['SAUNA_AT'], 
#         row['BNQTHL_AT'], row['BSINES_CNTER_AT'], row['BEACH_AT']
#     ))

# # 변경사항 커밋
# conn.commit()

# # 연결 닫기
# cursor.close()
# conn.close()