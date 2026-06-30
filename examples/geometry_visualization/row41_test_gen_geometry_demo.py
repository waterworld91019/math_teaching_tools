
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 定義長方體頂點 (x: 0~1, y: 0~2, z: 0~3)
cuboid_vertices = np.array([
    [0,0,0],  # 0
    [1,0,0],  # 1
    [1,2,0],  # 2
    [0,2,0],  # 3
    [0,0,3],  # 4
    [1,0,3],  # 5
    [1,2,3],  # 6
    [0,2,3]   # 7
])

# 長方體的邊（頂點索引）
cuboid_edges = [(0,1), (1,2), (2,3), (3,0),
                (4,5), (5,6), (6,7), (7,4),
                (0,4), (1,5), (2,6), (3,7)]

# 選取四面體的頂點：A(0,0,0), B(1,2,0), C(1,0,3), D(0,2,3)
tetra_indices = [0, 2, 5, 7]
tetra_vertices = cuboid_vertices[tetra_indices]

# 四面體的邊（在四個頂點之間連線）
tetra_edges = [(0,1), (0,2), (0,3),
               (1,2), (1,3), (2,3)]

# 創建 3D 圖形
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# 畫出長方體（虛線表示）
for edge in cuboid_edges:
    points = cuboid_vertices[list(edge)]
    ax.plot(points[:,0], points[:,1], points[:,2], color='gray', linestyle='--', linewidth=1)

# 畫出四面體（實線表示）
for edge in tetra_edges:
    points = tetra_vertices[list(edge)]
    ax.plot(points[:,0], points[:,1], points[:,2], color='red', linewidth=2)

# 畫出四面體的頂點
ax.scatter(tetra_vertices[:,0], tetra_vertices[:,1], tetra_vertices[:,2], color='red', s=50)

# 標記頂點
labels = ['A (0,0,0)', 'B (1,2,0)', 'C (1,0,3)', 'D (0,2,3)']
for i, label in enumerate(labels):
    ax.text(tetra_vertices[i,0], tetra_vertices[i,1], tetra_vertices[i,2], label, size=10, color='black')

# 設定坐標軸標籤與標題
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('長方體內的四面體（各面全等）')

# 設定坐標軸比例
ax.set_box_aspect([1,2,3])

plt.show()
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# 定義正立方體頂點 (A, B, C, D, E, F, G, H)
vertices = np.array([
    [0, 0, 0],  # A
    [1, 0, 0],  # B
    [1, 1, 0],  # C
    [0, 1, 0],  # D
    [0, 0, 1],  # E
    [1, 0, 1],  # F
    [1, 1, 1],  # G
    [0, 1, 1]   # H
])

# 定義正立方體的邊（依據頂點索引）
edges = [
    (0,1), (1,2), (2,3), (3,0),   # 底面邊：A, B, C, D
    (4,5), (5,6), (6,7), (7,4),   # 上面邊：E, F, G, H
    (0,4), (1,5), (2,6), (3,7)    # 連接底面與上面的邊
]

# 創建 3D 圖形
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# 畫出正立方體的邊（藍色線段）
for edge in edges:
    pts = vertices[list(edge)]
    ax.plot(pts[:,0], pts[:,1], pts[:,2], 'b-', linewidth=2)

# 畫出線段 AG (從 A 到 G)
A = vertices[0]  # A: (0,0,0)
G = vertices[6]  # G: (1,1,1)
line_AG = np.array([A, G])
ax.plot(line_AG[:,0], line_AG[:,1], line_AG[:,2], 'r-', linewidth=2, label='AG')

# 畫出平面 BDE (由頂點 B, D, E 組成)
B = vertices[1]  # B: (1,0,0)
D = vertices[3]  # D: (0,1,0)
E = vertices[4]  # E: (0,0,1)
triangle_BDE = [B, D, E]
poly_BDE = Poly3DCollection([triangle_BDE], color='green', alpha=0.3)
ax.add_collection3d(poly_BDE)

# 畫出平面 CFH (由頂點 C, F, H 組成)
C = vertices[2]  # C: (1,1,0)
F = vertices[5]  # F: (1,0,1)
H = vertices[7]  # H: (0,1,1)
triangle_CFH = [C, F, H]
poly_CFH = Poly3DCollection([triangle_CFH], color='orange', alpha=0.3)
ax.add_collection3d(poly_CFH)

# 標記每個頂點
labels = ['A','B','C','D','E','F','G','H']
for i, label in enumerate(labels):
    ax.text(vertices[i,0], vertices[i,1], vertices[i,2], f' {label}', fontsize=12, color='k')

# 設定坐標軸標籤與標題
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('正立方體及附加元素：線 AG, 平面 BDE, 平面 CFH')

# 設定坐標軸比例相等
ax.set_box_aspect([1,1,1])

plt.legend()
plt.show()
'''