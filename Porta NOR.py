import random

trainingset = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1]]  # porta NOR
eta = 0.3  # passo de aprendizado
maxiterations = 100
w1 = random.uniform(-0.2 , 0.2)
w2 = random.uniform(-0.5, 0.5)
w0 = 1

error = random.uniform(-0.2, 0.2)
count = 0
def new_func(eta, w0, target, output):
    w0 += eta * (target - output)*(1)

while count < maxiterations and error != 0:
    error = 0
    for array in trainingset:
        target = array[2]
        output = 0
        summation = w1 * array[0] + w2 * array[1] - w0
        if (summation > 0):
            output = 1
        else:
            output = 0

        if (output != target):
            error += 1

        w1 += eta * (target - output) * array[0]  # regra delta
        w2 += eta * (target - output) * array[1]
        w0 += eta * (target - output)*(-1)

        print("Saída " + str(output) + " target " + str(target))
        print("Erro " + str(error))
    count += 1
print("Iterações: " + str(count))
print("Erro final: " + str(error))
print("w1: " + str(w1) + ", w2: " + str(w2) + ", w0: " + str(w0))