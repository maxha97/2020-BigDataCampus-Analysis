import ExamList as el
# import ExamVo as ee


class ExamOop:
    def main(self):
        lists = el.ExamList()
        while True:
            menu = self.print_menu()
            if (menu == 1):
                lists.input_exam()
            elif (menu == 2):
                lists.print_exam()
            elif (menu == 3):
                print("Bye~~")
                break
            else:
                print("잘못된 값을 입력하셨습니다. 메뉴는 1~3까지입니다.")

    def print_menu(self):
        print("┌───────────────────────────┐")
        print("│        메인 메뉴          │")
        print("└───────────────────────────┘")
        print("1. 성적입력")
        print("2. 성적출력")
        print("3. 종료")
        print("선택>", end=" ")
        menu = int(input())
        return menu

    # def input_exam(self, list):
    #     print("┌───────────────────────────┐")
    #     print("│        성적  입력         │")
    #     print("└───────────────────────────┘")

    #     i = list.current+1
    #     while True:
    #         kor = int(input("국어 %d : " % i))

    #         if (0 > kor or 100 < kor):
    #             print("국어성적은 0~100까지의 범위만 입력이 가능합니다.")
    #         if(0 <= kor and 100 >= kor):
    #             break
    #     while True:
    #         eng = int(input("영어 %d : " % i))

    #         if (0 > eng or 100 < eng):
    #             print("영어성적은 0~100까지의 범위만 입력이 가능합니다.")
    #         if(0 <= eng and 100 >= eng):
    #             break
    #     while True:
    #         math = int(input("수학 %d : " % i))

    #         if (0 > math or 100 < math):
    #             print("수학성적은 0~100까지의 범위만 입력이 가능합니다.")
    #         if(0 <= math and 100 >= math):
    #             break
    #     exam = ee.ExamVo()
    #     exam.kor = kor
    #     exam.eng = eng
    #     exam.math = math
    #     list.current = list.current + 1
    #     list.list.append(exam)
    #     print("─────────────────────────────")

    # def print_exam(self, list):
    #     print("┌───────────────────────────┐")
    #     print("│        성적  출력         │")
    #     print("└───────────────────────────┘")
    #     # for i, exam in enumerate(self.get_list()):
    #     for i in range(len(self.get_list())):
    #         exam = self.get_list()[i]
    #         kor = exam.kor
    #         eng = exam.eng
    #         math = exam.math
    #         total = kor + eng + math

    #         avg = total / 3.0

    #         print("[국어 %d : %3d]  " % (i+1, kor), end=" ")
    #         print("[영어 %d : %3d]  " % (i+1, eng), end=" ")
    #         print("[수학 %d : %3d]  " % (i+1, math), end=" ")

    #         print("\n[총점 : %3d]" % total)
    #         print("[평균 : %6.2f]" % avg)
    #         print("─────────────────────────────")


if __name__ == "__main__":
    exam = ExamOop()
    exam.main()
