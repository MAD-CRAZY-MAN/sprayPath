from geopy.distance import geodesic
from geopy.point import Point
import csv


def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).meters

def calculate_midpoint(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # 위도, 경도의 중간 값 계산
    mid_lat = (lat1 + lat2) / 2
    mid_lon = (lon1 + lon2) / 2

    # Point 객체 생성
    midpoint = Point(mid_lat, mid_lon)

    return midpoint

def read_coordinates_from_csv(filename):
    coordinates = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            coordinates[row['id']] = {
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude'])
            }
    return coordinates

def get_coordinates_by_id(coordinates, id):
    if id in coordinates:
        return coordinates[id]
    else:
        return None

# CSV 파일에서 좌표 읽기
filename = '../examples/converted_coordinates.csv'  # CSV 파일 경로
coordinates = read_coordinates_from_csv(filename)

# id 입력 받기
id1 = input("첫번째 ID를 입력하세요: ")
id2 = input("두번째 ID를 입력하세요: ")

# 해당 id에 대한 좌표 조회
coordinate1 = get_coordinates_by_id(coordinates, id1)
coordinate2 = get_coordinates_by_id(coordinates, id2)

if coordinate1:
    print("위도:", coordinate1['latitude'])
    print("경도:", coordinate1['longitude'])
else:
    print("첫번째 ID에 대한 좌표를 찾을 수 없습니다.")

if coordinate2:
    print("위도:", coordinate2['latitude'])
    print("경도:", coordinate2['longitude'])
else:
    print("첫번째 ID에 대한 좌표를 찾을 수 없습니다.")
# 입력 좌표 받기
# lat1 = float(input("첫 번째 위도 입력: "))
# lon1 = float(input("첫 번째 경도 입력: "))
# lat2 = float(input("두 번째 위도 입력: "))
# lon2 = float(input("두 번째 경도 입력: "))
lat1 = coordinate1['latitude']
lon1 = coordinate1['longitude']
lat2 = coordinate2['latitude']
lon2 = coordinate2['longitude']

# 좌표 형식으로 변환
coord1 = (lat1, lon1)
coord2 = (lat2, lon2)

# 거리 계산
distance = calculate_distance(coord1, coord2)
print("두 좌표 사이의 거리:", distance, "미터")

# 중간 지점 계산
midpoint = calculate_midpoint(coord1, coord2)
print("두 좌표 중간 지점의 좌표:", midpoint.latitude, midpoint.longitude)
