def create_dict(filename):
    subject_dict = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:

            subject, activities = line.split(':')
            total_classes = 0

            for activity in activities.split():
                count = int(activity.split('(')[0])
                total_classes += count

            subject_dict[subject] = total_classes

    return subject_dict




subject_dict = create_dict('Предметы.txt')
print(subject_dict)


