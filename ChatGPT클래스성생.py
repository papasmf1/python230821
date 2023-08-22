# 기본 클래스인 Person을 정의합니다.
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print("ID:", self.id)
        print("이름:", self.name)

# Person을 상속받은 Manager 클래스를 정의합니다.
class Manager(Person):
    def __init__(self, id, name, skill, role):
        super().__init__(id, name)
        self.skill = skill
        self.role = role

# Person을 상속받은 Employee 클래스를 정의합니다.
class Employee(Person):
    def __init__(self, id, name, role):
        super().__init__(id, name)
        self.role = role

# 테스트용 예제 코드

# 1. 매니저 생성 및 정보 출력
manager = Manager(id=1, name="Alice", skill="팀 관리", role="프로젝트 매니저")
manager.printInfo()
print("기술:", manager.skill)
print("역할:", manager.role)
print()

# 2. 직원 생성 및 정보 출력
employee = Employee(id=2, name="Bob", role="소프트웨어 엔지니어")
employee.printInfo()
print("역할:", employee.role)
print()

# ... (다른 예제 코드 스니펫)

# 10. 직원과 매니저 인스턴스를 혼합하여 테스트
people_mixed = [
    Employee(id=15, name="Oliver", role="품질 보증 테스터"),
    Manager(id=16, name="Patricia", skill="갈등 해결", role="팀 리더"),
    Employee(id=17, name="Quincy", role="백엔드 개발자"),
    Manager(id=18, name="Rachel", skill="예산 관리", role="재무 매니저"),
    Manager(id=19, name="Sam", skill="전략적 기획", role="마케팅 매니저"),
    Employee(id=20, name="Taylor", role="프론트엔드 개발자")
]

for person in people_mixed:
    person.printInfo()
    if isinstance(person, Manager):
        print("기술:", person.skill)
    print("역할:", person.role)
    print()
