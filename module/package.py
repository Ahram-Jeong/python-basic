# # import는 package, module 까지만 가능! class, 함수는 import 불가능
# import travel.france
# trip1 = travel.france.FrancePackage()
# trip1.detail()
#
# # from-import 구문에서는 모두 가능
# from travel.sweden import SwedenPackage
# trip2 = SwedenPackage()
# trip2.detail()
#
# from travel import france
# trip3 = france.FrancePackage()
# trip3.detail()

# from 패키지 단위로 import 할 경우, __init__ 파일 내 __all__로 지정된 모듈만 import가 가능
from travel import *
# trip4 = france.FrancePackage()
# trip5 = sweden.SwedenPackage()
# trip4.detail()
# trip5.detail()

# 패키지와 모듈의 경로 찾기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(sweden))