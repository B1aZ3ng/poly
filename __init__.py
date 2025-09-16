import random
import gymnasium as gym
from gymnasium import spaces

GRID_SIZE = 8
INIT_HEALTH = 10
STAR_POINTS_PER_CENTER = 2

class Tile:
    def __init__(self):
        self.center = None
        self.warrior = None

class Warrior:
    def __init__(self, owner):
        self.owner = owner
        self.health = INIT_HEALTH
        self.max_health = INIT_HEALTH
        self.attack = 3
        self.defense = 3

class Center:
    def __init__(self, owner):
        self.owner = owner

class PolytopiaEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(PolytopiaEnv, self).__init__()
        self.grid = [[Tile() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.players = ["Player1", "Player2"]
        self.current_player = 0

        self.action_space = spaces.Discrete(GRID_SIZE * GRID_SIZE * 2)
        self.observation_space = spaces.Box(low=0, high=3, shape=(GRID_SIZE, GRID_SIZE), dtype=int)

        self.init_map()

    def init_map(self):
        self.grid[0][0].center = Center(self.players[0])
        self.grid[GRID_SIZE-1][GRID_SIZE-1].center = Center(self.players[1])

    def spawn_warrior(self, x, y):
        tile = self.grid[x][y]
        if tile.center and tile.center.owner == self.players[self.current_player]:
            if tile.warrior:
                self.shift_warrior(x, y)
            tile.warrior = Warrior(tile.center.owner)

    def shift_warrior(self, x, y):
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.grid[nx][ny].warrior is None:
                self.grid[nx][ny].warrior = self.grid[x][y].warrior
                return

    def attack(self, ax, ay, dx, dy):
        attacker = self.grid[ax][ay].warrior
        defender = self.grid[dx][dy].warrior
        if attacker and defender and attacker.owner != defender.owner:
            defense_bonus = 1.0
            attack_force = attacker.attack * (attacker.health / attacker.max_health)
            defense_force = defender.defense * (defender.health / defender.max_health) * defense_bonus
            total_force = attack_force + defense_force

            attack_result = round((attack_force / total_force) * attacker.attack * 4.5)
            defense_result = round((defense_force / total_force) * defender.defense * 4.5)

            defender.health -= attack_result
            attacker.health -= defense_result

            if defender.health <= 0:
                self.grid[dx][dy].warrior = None
            if attacker.health <= 0:
                self.grid[ax][ay].warrior = None

    def step(self, action):
        act_type = action // (GRID_SIZE * GRID_SIZE)
        pos = action % (GRID_SIZE * GRID_SIZE)
        x, y = pos % GRID_SIZE, pos // GRID_SIZE

        if act_type == 0:
            self.spawn_warrior(x, y)
        else:
            if x+1 < GRID_SIZE:
                self.attack(x, y, x+1, y)

        obs = self.get_obs()
        reward = self.calculate_reward()
        done = False
        info = {}
        self.current_player = 1 - self.current_player
        return obs, reward, done, False, info

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.grid = [[Tile() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.init_map()
        self.current_player = 0
        return self.get_obs(), {}

    def get_obs(self):
        obs = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                tile = self.grid[x][y]
                if tile.center:
                    obs[y][x] = 1
                elif tile.warrior:
                    obs[y][x] = 2 if tile.warrior.owner == self.players[0] else 3
        return obs

    def calculate_reward(self):
        center_count = sum(1 for row in self.grid for t in row if t.center and t.center.owner == self.players[self.current_player])
        return center_count * STAR_POINTS_PER_CENTER

    def render(self):
        for y in range(GRID_SIZE):
            row = ""
            for x in range(GRID_SIZE):
                tile = self.grid[x][y]
                if tile.center:
                    row += "C1 " if tile.center.owner == self.players[0] else "C2 "
                elif tile.warrior:
                    row += "W1 " if tile.warrior.owner == self.players[0] else "W2 "
                else:
                    row += ". "
            print(row)
        print("\n")