from character.py import Hero, Monster # type: ignore
from battle.py import Battle # type: ignore

def main():
    print("=== RPG 게임 ===")
    name = input("영웅의 이름을 입력하세요: ")
    role = input("직업을 선택하세요 (전사/마법사/궁수): ")
    hero = Hero(name, hp=100, attack=20, defense=5, role=role)
    print(f"\n{hero.name} ({hero.role})이(가) 생성되었습니다!")
    print(hero)

    # 몬스터 생성
    monster = Monster(name="고블린", hp=50, attack=10, defense=2)
    print(f"\n몬스터 {monster.name}이(가) 등장했습니다!")
    print(monster)

    # 전투
    battle = Battle()
    battle.fight(hero, monster)

    # 영웅 상태 출력
    print("\n전투 후 영웅 상태:")
    print(hero)

if __name__ == "__main__":
    main()