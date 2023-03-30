import file_operations
from faker import Faker
import random

runic_skills = [
    'С͒т͒͒р̋̋͠͠е͠͠м͒͠ит͒͒е͠͠л̋͠ь̋н͒ы̋̋͠͠й͒͠ п̋͠р̋̋͠͠ы̋̋͠͠ж͒о̋к̋̋',
    'Э͒͠͠л̋̋͠͠е͠͠͠к̋̋̋̋т͒͒р̋̋͠͠ич̋͠е͠͠͠с͒͒к̋̋̋̋ий'
    '͒͠ в͒͠ы̋͠с͒͒т͒͒р̋̋͠͠е͠͠͠л̋̋͠͠',
    'Л̋͠е͠д̋̋я̋н͒о̋й͒͠ у͒͠д̋̋а͠р̋͠',
    'С͒т͒͒р̋̋͠͠е͠͠м͒͠ит͒͒е͠͠л̋͠ь̋н͒ы̋͠й͒͠ у͒͠д̋а͠р̋̋͠͠',
    'К̋̋ис͒л̋̋͠͠о̋т͒н͒ы̋͠й͒͠ в͒͠з̋̋͠г͒͠л̋̋͠͠я̋д̋',
    'Т͒а͠й͒͒͠͠н͒ы̋͠й͒͒͠͠ п̋͠о̋б̋е͠г͒͠',
    'Л̋͠е͠͠д̋я̋н͒о̋й͒͠ в͒͠ы̋͠с͒т͒р̋͠е͠͠л̋͠'
]


def main():
    fake = Faker('ru_RU')
    for n in range(1, 11):
        random_skills = random.sample(runic_skills, 3)
        content = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'luck': random.randint(3, 18),
            'skill_1': random_skills[0],
            'skill_2': random_skills[1],
            'skill_3': random_skills[2]
        }
        file_operations.render_template(
            'charsheet.svg',
            f"карточки игроков/card{n}.svg",
            content
        )


if __name__ == '__main__':
    main()
