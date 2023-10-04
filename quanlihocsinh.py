class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class QuanLiHocSinh:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_all_students(self):
        return self.students

def main():
    manager = QuanLiHocSinh()

    while True:
        print("\n===== Quản lí học sinh =====")
        print("1. Thêm học sinh")
        print("2. Xóa học sinh")
        print("3. Hiển thị danh sách học sinh")
        print("0. Thoát")
        choice = input("Chọn một tác vụ: ")

        if choice == '1':
            name = input("Nhập tên học sinh: ")
            age = input("Nhập tuổi học sinh: ")
            grade = input("Nhập lớp học sinh: ")
            student = Student(name, age, grade)
            manager.add_student(student)
            print("Đã thêm học sinh thành công!")
        elif choice == '2':
            students = manager.get_all_students()
            if students:
                print("Danh sách học sinh:")
                for index, student in enumerate(students):
                    print(f"{index + 1}. {student.name} - {student.age} tuổi - Lớp {student.grade}")
                student_index = input("Chọn số thứ tự học sinh muốn xóa: ")
                if student_index.isdigit():
                    student_index = int(student_index)
                    if student_index >= 1 and student_index <= len(students):
                        student = students[student_index - 1]
                        manager.remove_student(student)
                        print("Đã xóa học sinh thành công!")
                    else:
                        print("Số thứ tự không hợp lệ!")
                else:
                    print("Số thứ tự không hợp lệ!")
            else:
                print("Không có học sinh nào trong danh sách.")
        elif choice == '3':
            students = manager.get_all_students()
            if students:
                print("Danh sách học sinh:")
                for index, student in enumerate(students):
                    print(f"{index + 1}. {student.name} - {student.age} tuổi - Lớp {student.grade}")
            else:
                print("Không có học sinh nào trong danh sách.")
        elif choice == '0':
            break
        else:
            print("Lựachọn không hợp lệ!")

if __name__ == '__main__':
    main()