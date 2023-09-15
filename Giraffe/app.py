from Questions import Questions

prompts = [
    "Qual a cor do céu?\na) Azul\nb) Laranja",
    "Qual a velocidade da luz?\na) altíssima\n b) lentíssima",
    "Qual a profissão do Silvio Santos?\na) Comunicador\nb) Programador"
]

questions = [
    Questions("Qual a cor do céu?\na) Azul\nb) Laranja", "a"),
    Questions(prompts[1], "a"),
    Questions(prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questions.question_prompt)
        if answer == questions.cor_answer:
            score =+ 1
    print(str(score))

def raise_to_power(base_num, pow_num):
    base = 1
    for index in range(pow_num):
        base = base * base_num
    return base

run_test(questions)
#print(raise_to_power(2, 3))
