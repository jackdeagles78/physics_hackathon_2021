import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import imageio
import glob

def apply_gravity(theta, t, g, m, k):
    y1, vy1 = theta
    dthetadt = [vy1, -m*g-y1*k]
    return dthetadt


def apply_physics(positions, velocities, dx, dt, m, T):
    # Take an input array of positions, apply the physics on each point, and determine
    # the new positions after a time dt
    n = len(positions)
    new_positions = [0,0] # the second zero will be changed
    new_velocities = [0,0] # the second zero will be changed
    for i in range(2,n-1):
        # Find displacement on right/left side
        ldisp = positions(i-1)
        rdisp = positions(i+1)
        curdisp = positions(i)
        # Next compute the gradients. We will not use the approximation!
        sintheta = np.arcsin((curdisp - ldisp)/dx)
        sinpsi = np.arcsin((curdisp - rdisp)/dx)
        # Now we have that the equation of motion is m(acc) = -T(sintheta + sinpsi)
        # acc = -T/m * (sintheta + sinpsi)
        acc = -T/m * (sintheta + sinpsi)
        v = acc * dt
        s = curdisp*velocities(i) + 0.5 * acc * (dt**2)
        new_positions[i] = s
        new_velocities[i] = v 

    new_positions.append(0)
    new_velocities.append(0)

def main():
<<<<<<< HEAD
    plt.plot 
=======
    print("Hello World")
    g = 10
    m = 1
    k = 1
    t = np.linspace(0,5,20)
    theta0 = (-5,0)

    sol = odeint(apply_gravity, theta0, t, args=(g, m, k))
    fig, ax = plt.subplots()
    ax.plot(t, sol[:, 0], label="position1")
    plt.legend()
    plt.show()

    images = []
    ymin, ymax = np.min(sol[:,0]), np.max(sol[:,0])
    for i in range(len(sol)):
        fig, ax = plt.subplots()
        plt.ylim(ymin-1, ymax+1)
        ax.scatter(0, sol[i][0], label="position1")
        plt.legend()
        fname = f"tmp/tmp.png"
        plt.savefig(fname)
        images.append(imageio.imread(fname))
    imageio.mimsave('movie.gif', images)
>>>>>>> 45fd26dfcdbefc011dee5fede871efb1a1efc81c


if __name__ == '__main__':
    main()
