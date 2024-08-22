import random

trainings = {
    'biceps': ['Rosca direta com barra', 'Rosca alternada com halteres', 'Rosca concentrada', 'Rosca martelo', 'Rosca inversa com barra'],
    'triceps': ['Tríceps pulley', 'Tríceps testa', 'Tríceps banco', 'Tríceps francês', 'Mergulho entre bancos'],
    'posterior_coxa': ['Cadeira flexora', 'Mesa flexora', 'Stiff', 'Good morning', 'Levantamento terra romeno'],
    'quadriceps': ['Agachamento livre', 'Leg press', 'Cadeira extensora', 'Afundo com halteres', 'Agachamento no Smith'],
    'costas': ['Remada curvada', 'Puxada alta', 'Remada cavalinho', 'Levantamento terra', 'Pull-up (barra fixa)'],
    'peito': ['Supino reto', 'Supino inclinado', 'Crucifixo com halteres', 'Supino declinado', 'Cross over']
}


def training_sorter(training_day, rep):
    list_trainings = trainings.get(training_day)
    if list_trainings is None:
        return 'Treino não configurado no sistema.'
    
    if rep is None or rep <= 0:
        return 'Informe uma quantidade válida de séries.'
    
    random.shuffle(list_trainings)
    return list_trainings[0:rep]


if __name__ == '__main__':
    training = 'triceps'
    rep = 2
    print(training_sorter(training, rep))