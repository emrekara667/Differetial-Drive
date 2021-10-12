import matplotlib.pyplot as plt
import numpy as np
import time

print("Emre Kara")

animation = True

def plot_vehicle(x_n, y_n, theta_bas, x_rec, y_rec):
    start_1 = np.array([0.25, 0, 1])
    start_2 = np.array([-0.25, 0.15, 1])
    start_3 = np.array([-0.25, -0.15, 1])

    T = transformation_matrix(x_n, y_n, theta_bas)
    p1 = np.matmul(T, start_1)
    p2 = np.matmul(T, start_2)
    p3 = np.matmul(T, start_3)

    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', marker='.', linestyle='-')
    plt.plot([p2[0], p3[0]], [p2[1], p3[1]], color='green', marker='.', linestyle='-')
    plt.plot([p3[0], p1[0]], [p3[1], p1[1]], color='green', marker='.', linestyle='-')

    plt.plot(x_rec, y_rec, ',r')

    plt.gcf()

    plt.xlim(-1, 10)
    plt.ylim(-1.5, 10)

    plt.pause(dt)


def transformation_matrix(x_n, y_n, theta_bas):
    return np.array([
        [np.cos(theta_bas), -np.sin(theta_bas), x_n],
        [np.sin(theta_bas), np.cos(theta_bas), y_n],
        [0, 0, 1]
    ])


def hiz_hesapla(w_r, w_l):
    v_r = w_r * R / 2
    v_l = w_l * R / 2
    return v_r, v_l

#x, y, theta, x_ekseni, y_ekseni = hareket(x_baslangic, y_baslangic, theta_baslangic, v_r, v_l, l, t, dt,x_ekseni, y_ekseni)
def hareket(x_bas, y_bas, theta_bas, v_r, v_l, L, Time, dt, x_yorunge, y_yorunge):

    ilk_zaman = time.time()

    while True:
        ikinci_zaman = time.time()
        w = (v_r - v_l) / L
        theta_bas = theta_bas + w * dt
        x_bas = x_bas + (1/2) * (v_r + v_l) * dt * np.cos(theta_bas)
        y_bas = y_bas + (1/2) * (v_r + v_l) * dt * np.sin(theta_bas)

        x_yorunge.append(x_bas)
        y_yorunge.append(y_bas)
        dt += 0.1

        if animation:
            plt.cla()
            plot_vehicle(x_bas, y_bas, theta_bas, x_yorunge, y_yorunge)
        if ikinci_zaman - ilk_zaman  > Time:
            break
    return x_bas, y_bas, theta_bas, x_yorunge, y_yorunge




R = 0.1
l = 0.3
x_baslangic = 0
y_baslangic = 0
theta_baslangic = 0
dt = 0.1
x_ekseni, y_ekseni = [], []

# 1. hareket w_r = 10 w_l = 10
w_r = 10
w_l = 10
v_r,v_l = hiz_hesapla(w_r, w_l)
t = 5
x, y, theta, x_ekseni, y_ekseni = hareket(x_baslangic, y_baslangic, theta_baslangic, v_r, v_l, l, t, dt,x_ekseni, y_ekseni)
# 2. hareket w_r = 5 w_l = 10
w_r = 5
w_l = 10
v_r,v_l = hiz_hesapla(w_r, w_l)
t = 5
x, y, theta, x_ekseni, y_ekseni = hareket(x, y, theta, v_r, v_l, l, t, dt, x_ekseni, y_ekseni)
# 3. hareket w_r = 5 w_l = 10
w_r = 10
w_l = -10
v_r,v_l = hiz_hesapla(w_r, w_l)
t = 5
x, y, theta, x_ekseni, y_ekseni = hareket(x, y, theta, v_r, v_l, l, t, dt, x_ekseni, y_ekseni)
# 4. hareket w_r = 5 w_l = 10
w_r = 0
w_l = 10
v_r,v_l = hiz_hesapla(w_r, w_l)
t = 5
x, y, theta, x_ekseni, y_ekseni = hareket(x, y, theta, v_r, v_l, l, t, dt, x_ekseni, y_ekseni)
