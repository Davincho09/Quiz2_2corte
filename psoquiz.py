import numpy as np
import matplotlib.pyplot as plt

area_size = 5000  
num_drones = 10
sensor_radius = 200  
max_iter = 50        
num_particles = 30   
w, c1, c2 = 0.7, 1.5, 1.5 

grid_size = 50
prob_map = np.random.rand(grid_size, grid_size)


def fitness(positions):
    coverage = np.zeros_like(prob_map)
    for drone in positions:
        x, y = int(drone[0] / (area_size/grid_size)), int(drone[1] / (area_size/grid_size))
        for i in range(grid_size):
            for j in range(grid_size):
                dist = np.sqrt((i-x)**2 + (j-y)**2)
                if dist * (area_size/grid_size) <= sensor_radius:
                    coverage[i, j] = 1
    return np.sum(prob_map * coverage)

particles = np.random.rand(num_particles, num_drones, 2) * area_size
velocities = np.random.randn(num_particles, num_drones, 2)
pbest_positions = particles.copy()
pbest_scores = np.array([fitness(p) for p in particles])
gbest_position = pbest_positions[np.argmax(pbest_scores)]
gbest_score = np.max(pbest_scores)

for t in range(max_iter):
    for i in range(num_particles):
        r1, r2 = np.random.rand(), np.random.rand()
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest_positions[i] - particles[i])
            + c2 * r2 * (gbest_position - particles[i])
        )
        particles[i] += velocities[i]
    
        particles[i] = np.clip(particles[i], 0, area_size)

     
        score = fitness(particles[i])
        if score > pbest_scores[i]:
            pbest_scores[i] = score
            pbest_positions[i] = particles[i].copy()
   
    best_idx = np.argmax(pbest_scores)
    if pbest_scores[best_idx] > gbest_score:
        gbest_score = pbest_scores[best_idx]
        gbest_position = pbest_positions[best_idx].copy()

    print(f"Iteración {t+1}/{max_iter} -> Mejor resultado: {gbest_score}")

plt.imshow(prob_map, cmap="hot", interpolation="nearest", extent=[0, area_size, 0, area_size])
for drone in gbest_position:
    plt.scatter(drone[0], drone[1], c="cyan", edgecolors="black")
plt.title("Posiciones de los drones")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.colorbar(label="Probabilidad de sobrevivientes")
plt.show()
