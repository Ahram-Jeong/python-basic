class FrancePackage :
    def detail(self):
        print("[파리 패키지 7박 9일] 파리 미술관 투어 200만원")

if __name__ == "__main__" :
    print("===== 모듈을 직접 실행 =====")
    trip_to = FrancePackage()
    trip_to.detail()
else :
    print("===== 외부에서 모듈 호출 =====")