# %%
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# %%
ON = 255
OFF = 0
vals = [ON, OFF]
# %%
def randomGrid(N):
    return np.random.choice(vals, N*N, p=[0.1,0.9]).reshape(N, N)

# %%
def addGlider(i, j, grid):
    glider = np.array([[0,0,255],
                       [255,0,255],
                       [0,255,255]])
    grid[i:i+3, j:j+3] = glider
# %%
def update(frameNum, img, grid, N):

    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            
            #Computes eight-neighbor sum
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N])/255)

            #Conway's Rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    #update grid
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# %%
def main():

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life.")

    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    args = parser.parse_args()

    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    grid = np.array([])

    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    else:
        grid = randomGrid(N)
 
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, 
                                  fargs=(img, grid, N),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)
 
    # # of frames? 
    # set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
 
    plt.show()
# %%
if __name__ == '__main__':
    main()
# %%
