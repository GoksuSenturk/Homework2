import numpy as np
import random

num_iter = 100  # döngü sayısı
tabu_len = 18  # tabu listesi uzunlugu
# lst_len = random.randint(7, 20) # dynamic list size
sol_len = 20  # çözüm arrayinin uzunluğu
N = 190  # max komşu çözüm kombinasyon sayısı

flow = [[0, 0, 5, 0, 5, 2, 10, 3, 1, 5, 5, 5, 0, 0, 5, 4, 4, 0, 0, 1],
        [0, 0, 3, 10, 5, 1, 5, 1, 2, 4, 2, 5, 0, 10, 10, 3, 0, 5, 10, 5],
        [5, 3, 0, 2, 0, 5, 2, 4, 4, 5, 0, 0, 0, 5, 1, 0, 0, 5, 0, 0],
        [0, 10, 2, 0, 1, 0, 5, 2, 1, 0, 10, 2, 2, 0, 2, 1, 5, 2, 5, 5],
        [5, 5, 0, 1, 0, 5, 6, 5, 2, 5, 2, 0, 5, 1, 1, 1, 5, 2, 5, 1],
        [2, 1, 5, 0, 5, 0, 5, 2, 1, 6, 0, 0, 10, 0, 2, 0, 1, 0, 1, 5],
        [10, 5, 2, 5, 6, 5, 0, 0, 0, 0, 5, 10, 2, 2, 5, 1, 2, 1, 0, 10],
        [3, 1, 4, 2, 5, 2, 0, 0, 1, 1, 10, 10, 2, 0, 10, 2, 5, 2, 2, 10],
        [1, 2, 4, 1, 2, 1, 0, 1, 0, 2, 0, 3, 5, 5, 0, 5, 0, 0, 0, 2],
        [5, 4, 5, 0, 5, 6, 0, 1, 2, 0, 5, 5, 0, 5, 1, 0, 0, 5, 5, 2],
        [5, 2, 0, 10, 2, 0, 5, 10, 0, 5, 0, 5, 2, 5, 1, 10, 0, 2, 2, 5],
        [5, 5, 0, 2, 0, 0, 10, 10, 3, 5, 5, 0, 2, 10, 5, 0, 1, 1, 2, 5],
        [0, 0, 0, 2, 5, 10, 2, 2, 5, 0, 2, 2, 0, 2, 2, 1, 0, 0, 0, 5],
        [0, 10, 5, 0, 1, 0, 2, 0, 5, 5, 5, 10, 2, 0, 5, 5, 1, 5, 5, 0],
        [5, 10, 1, 2, 1, 2, 5, 10, 0, 1, 1, 5, 2, 5, 0, 3, 0, 5, 10, 10],
        [4, 3, 0, 1, 1, 0, 1, 2, 5, 0, 10, 0, 1, 5, 3, 0, 0, 0, 2, 0],
        [4, 0, 0, 5, 5, 1, 2, 5, 0, 0, 0, 1, 0, 1, 0, 0, 0, 5, 2, 0],
        [0, 5, 5, 2, 2, 0, 1, 2, 0, 5, 2, 1, 0, 5, 5, 0, 5, 0, 1, 1],
        [0, 10, 0, 5, 5, 1, 0, 2, 0, 5, 2, 2, 0, 5, 10, 2, 2, 1, 0, 6],
        [1, 5, 0, 5, 1, 5, 10, 10, 2, 2, 5, 5, 5, 0, 10, 0, 0, 1, 6, 0]]

Distance = [[0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
            [1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 6],
            [2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5],
            [3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3, 6, 5, 4, 3, 4],
            [4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3],
            [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
            [2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5],
            [3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4],
            [4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3],
            [5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
            [2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5],
            [3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4],
            [4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3],
            [5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2],
            [6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1],
            [3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [4, 3, 4, 5, 6, 3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3],
            [5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2],
            [6, 5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1],
            [7, 6, 5, 4, 3, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0]]


def assignmt_cost(sol):
    cost = 0
    for i in range(sol_len):
        for j in range(sol_len):
            cost += Distance[i][j] * flow[sol[i]][sol[j]]
    return cost


neighbors = np.zeros((N, sol_len + 2), dtype=int)


def swap_move(sol_n):
    global idx, neighbors
    for i in range(sol_len):
        j = i + 1
        for j in range(sol_len):
            if i < j:
                idx = idx + 1
                sol_n[j], sol_n[i] = sol_n[i], sol_n[j]
                neighbors[idx, :-2] = sol_n
                neighbors[idx, -2:] = [sol_n[i], sol_n[j]]
                sol_n[i], sol_n[j] = sol_n[j], sol_n[i]


def not_in_tabu(solution, tabu):
    not_found = False
    if not solution.tolist() in tabu:
        solution[0], solution[1] = solution[1], solution[0]
        if not solution.tolist() in tabu:
            not_found = True

    return not_found


def run_tabu():
    global neighbors, num_iter, idx
    curnt_sol = random.sample(range(sol_len), sol_len)
    best_soln = curnt_sol
    Tabu = []
    frequency = {}

    print("Initial: %s cost %s " % (curnt_sol, assignmt_cost(curnt_sol)))  # başlangıç çözümünün amaç fonksiyonu
    while num_iter > 0:

        idx = -1
        swap_move(curnt_sol)  # komşuya bak

        cost = np.zeros((len(neighbors)))  # komşunun amaç fonksiyonu maliyetini tut
        for index in range(len(neighbors)):
            cost[index] = assignmt_cost(neighbors[index, :-2])  # aday komşunun maliyet fonksiyonunu değerlendir.
        rank = np.argsort(cost)  # maliyetleri sırala
        neighbors = neighbors[rank]

        for j in range(N):

            not_tabu = not_in_tabu(neighbors[j, -2:], Tabu)
            if (not_tabu):
                curnt_sol = neighbors[j, :-2].tolist()
                Tabu.append(neighbors[j, -2:].tolist())

                if len(Tabu) > tabu_len - 1:
                    Tabu = Tabu[1:]

                # frequency based
                if not tuple(curnt_sol) in frequency.keys():
                    frequency[tuple(curnt_sol)] = 1

                    if assignmt_cost(curnt_sol) < assignmt_cost(best_soln):
                        best_soln = curnt_sol

                else:

                    cur_cost = assignmt_cost(curnt_sol) + frequency[tuple(curnt_sol)]
                    frequency[tuple(curnt_sol)] += 1
                    if cur_cost < assignmt_cost(best_soln):
                        best_soln = curnt_sol

                break

            # Aspiration

            elif assignmt_cost(neighbors[j, :-2]) < assignmt_cost(best_soln):

                curnt_sol = neighbors[j, :-2].tolist()

                Tabu.insert(0, Tabu.pop(Tabu.index(neighbors[j, -2:].tolist())))

                # Tabu.append(neighbors[j, -2:].tolist())

                if len(Tabu) > tabu_len - 1:
                    Tabu = Tabu[1:]

                    # frequency based
                if not tuple(curnt_sol) in frequency.keys():
                    frequency[tuple(curnt_sol)] = 1
                    best_soln = curnt_sol

                else:

                    cur_cost = assignmt_cost(curnt_sol) + frequency[tuple(curnt_sol)]
                    frequency[tuple(curnt_sol)] += 1

                    if cur_cost < assignmt_cost(best_soln):
                        best_soln = curnt_sol

        num_iter -= 1
    print("Best sol %s cost: %s " % (best_soln, assignmt_cost(best_soln)))


if __name__ == "__main__":  # calling the main function, where the program starts running
    run_tabu()