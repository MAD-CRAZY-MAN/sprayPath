import json
import pandas as pd
from pyproj import CRS, Transformer

# JSON 파일 경로
json_file = '../examples/sample_geo.json'

# 변환할 좌표계 설정
epsg5186 = CRS.from_string("epsg:5186")
wgs84 = CRS.from_string("epsg:4326")
transformer = Transformer.from_crs(epsg5186, wgs84)

# JSON 파일 로드
with open(json_file, 'r') as file:
    json_data = json.load(file)

# 변환된 좌표와 id 저장할 리스트 생성
converted_coordinates = []

# JSON 데이터에서 좌표 변환 후 리스트에 추가
features = json_data['features']
for feature in features:
    feature_id = feature['id']
    coordinates = feature['geometry']['coordinates']
    y, x = coordinates
    lat, lon = transformer.transform(x, y)
    converted_coordinates.append({'id': feature_id, 'latitude': lat, 'longitude': lon})

# 변환된 좌표를 데이터프레임으로 생성
df = pd.DataFrame(converted_coordinates)

# CSV 파일로 저장
output_file = '../examples/converted_coordinates.csv'
df.to_csv(output_file, index=False)

print(f'변환된 좌표와 id가 {output_file}에 저장되었습니다.')
