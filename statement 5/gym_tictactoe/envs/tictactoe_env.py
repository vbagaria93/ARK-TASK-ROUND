import gym
from gym import error, spaces, utils
from gym.utils import seeding
import copy

def agent_by_mark(agents, mark):
  for agent in agents:
        if agent.mark == mark:
            return agent

def after_action_state(world, action):
    """Execute an action and returns resulted state.
    Args:
        world (list): 3 x 3 x 3 matrix
        action (tuple): [player] | [block] | [column] | [row]
    Returns:
        world (list): New 3 x 3 x 3 matrix with action applied
    """

    if action:
      if len(action) != 4:
        raise ValueError('Bad action: {}'.format(action))

      player, b, c, r = int(action[0]), int(action[1]), int(action[2]), int(action[3])
      
      if world[b][c][r] != 0:
        # If cell is in use, end game with reward of -1
         raise ValueError("Cannot mark an already marked position.")

      nworld = copy.deepcopy(world)
      nworld[b][c][r] = player

      return nworld


def check_game_status(world):
  """Return game status by current board status.
    Args:
        board (list): Current board state
    Returns:
        int:
            -1: game in progress,
            1 or 2 for finished game(winner mark code).
    """
  result = TicTacToeEnv._check(world)
  if result == None:
    return -1
  else:
    return result

class TicTacToeEnvKeys:
  KW_ENFORCE_ROUNDS = 'enforce_rounds'

class TicTacToeEnv(gym.Env):
  """
  TicTacToe environment:
    - World: 3 x 3 x 3 matrix
    - Players: 'x' and 'o'
    - Actions: [player] | [block] | [column] | [row]
  """
  metadata = {'render.modes': ['bcr','compact','full']}
  _EMPTY = '-'
  _X = 'x'
  _O = 'o'
  _PLAYERS = [_EMPTY, _X, _O]
  _PLAYERS_COUNT = 2
  _DIM_SIZE = 3
  _WORLDSIZE = _DIM_SIZE ** 3
  _MAX_ROUND = 3 * 3 * 3

  def __init__(self, **kwargs):
    self._round = 0
    self._result = None
    self._world = [[[self._get_empty(b, c, r) for r in range(TicTacToeEnv._DIM_SIZE)] for c in range(TicTacToeEnv._DIM_SIZE)] for b in range(TicTacToeEnv._DIM_SIZE)]
    self._done = True
    self.enforce_rounds = True
    if kwargs:
      self.enforce_rounds = kwargs[TicTacToeEnvKeys.KW_ENFORCE_ROUNDS] if TicTacToeEnvKeys.KW_ENFORCE_ROUNDS in kwargs else False
  
  def _get_empty(self, b, c, r):
    return 0

  def step(self, action):
    # Play the game only if action is not None
    if action:
      if len(action) != 4:
        raise ValueError('Bad action: {}'.format(action))

      player, b, c, r = int(action[0]), int(action[1]), int(action[2]), int(action[3])
      # if self._done:
      #   raise ValueError('Game has ended')
      
      if self.enforce_rounds and player != (self._round % TicTacToeEnv._PLAYERS_COUNT) + 1:
        raise ValueError('This is not {}\'s turn'.format(player))
      
      self._round += 1
      
      if self._world[b][c][r] != 0:
        # If cell is in use, end game with reward of -1
        self._done = True
        info = { 'round': self._round, 'next_player': 'NONE', 'error': 'Played occupied cell' }
        return self._world, -1, self._done, info

      self._world[b][c][r] = player
      # self._done = (_check() is not None) or (self._round == TicTacToeEnv._MAX_ROUND)
      self._result = TicTacToeEnv._check(self._world)
      self._done = (True if self._result else False)
      info = { 'round': self._round, 'next_player': 'NONE' if self._done else (self._round%TicTacToeEnv._PLAYERS_COUNT)+1 }
      return self._world, 1 if self._done else 0, self._done, info

  def get_as_char(self, b, c, r, winning_seq=None):
    val = self._world[b][c][r]
    ret = TicTacToeEnv._PLAYERS[val]

    if winning_seq and (b,c,r) in winning_seq:
      return ret.upper()
    else:
      return ret

  def reset(self):
    self._round = 0
    self._world = [[[self._get_empty(b, c, r) for r in range(TicTacToeEnv._DIM_SIZE)] for c in range(TicTacToeEnv._DIM_SIZE)] for b in range(TicTacToeEnv._DIM_SIZE)]
    self._done = False
    return self._world

  def render(self, mode='compact', close=False):
    # winning_seq = _check() if self._done else None

    for r in range(3):
      for b in range(3):
        for c in range(3):
            print(self.get_as_char(b, c, r), end=' ')
        print('   ', end='')
      print()

  def _check_indices(index1, index2, index3, world):
    a = world[index1[0]][index1[1]][index1[2]]
    if a == 0:
      return False

    b = world[index2[0]][index2[1]][index2[2]]
    if a != b:
      return False

    c = world[index3[0]][index3[1]][index3[2]]
    if b != c:
      return False
    
    return a

  def _check(world):
    # Naive implementation (for now)

    # For each block
    for b in range(3):
      # Check each column
      for c in range(3):
        if TicTacToeEnv._check_indices((b, c, 0), (b, c, 1), (b, c, 2), world):
          return TicTacToeEnv._check_indices((b, c, 0), (b, c, 1), (b, c, 2), world)
          # return sorted([(b, c, 0), (b, c, 1), (b, c, 2)])

      # Check each row
      for r in range(3):
        if TicTacToeEnv._check_indices((b, 0, r), (b, 1, r), (b, 2, r), world):
          return TicTacToeEnv._check_indices((b, 0, r), (b, 1, r), (b, 2, r), world)
          # return sorted([(b, 0, r), (b, 1, r), (b, 2, r)])

      if TicTacToeEnv._check_indices((b, 0, 0), (b, 1, 1), (b, 2, 2), world):
        return TicTacToeEnv._check_indices((b, 0, 0), (b, 1, 1), (b, 2, 2), world)
        # return sorted([(b, 0, 0), (b, 1, 1), (b, 2, 2)])

      if TicTacToeEnv._check_indices((b, 0, 2), (b, 1, 1), (b, 2, 0), world):
        return TicTacToeEnv._check_indices((b, 0, 2), (b, 1, 1), (b, 2, 0), world)
        # return sorted([(b, 0, 2), (b, 1, 1), (b, 2, 0)])

    # For each row
    for r in range(3):
      # Check each column
      for c in range(3):
        if TicTacToeEnv._check_indices((0, c, r), (1, c, r), (2, c, r), world):
          return TicTacToeEnv._check_indices((0, c, r), (1, c, r), (2, c, r), world)
          # return sorted([(0, c, r), (1, c, r), (2, c, r)])

      # Check each block
      for b in range(3):
        if TicTacToeEnv._check_indices((b, 0, r), (b, 1, r), (b, 2, r), world):
          return TicTacToeEnv._check_indices((b, 0, r), (b, 1, r), (b, 2, r), world)
          # return sorted([(b, 0, r), (b, 1, r), (b, 2, r)])

      if TicTacToeEnv._check_indices((0, 0, r), (1, 1, r), (2, 2, r), world):
        return TicTacToeEnv._check_indices((0, 0, r), (1, 1, r), (2, 2, r), world)
        # return sorted([(0, 0, r), (1, 1, r), (2, 2, r)])

      if TicTacToeEnv._check_indices((2, 0, r), (1, 1, r), (0, 2, r), world):
        return TicTacToeEnv._check_indices((2, 0, r), (1, 1, r), (0, 2, r), world)
        # return sorted([(2, 0, r), (1, 1, r), (0, 2, r)])

    # For each column
    for c in range(3):
      # Check each block
      for b in range(3):
        if TicTacToeEnv._check_indices((b, c, 0), (b, c, 1), (b, c, 2), world):
          return TicTacToeEnv._check_indices((b, c, 0), (b, c, 1), (b, c, 2), world)
          # return sorted([(b, c, 0), (b, c, 1), (b, c, 2)])

      # Check each row
      for r in range(3):
        if TicTacToeEnv._check_indices((0, c, r), (1, c, r), (2, c, r), world):
          return TicTacToeEnv._check_indices((0, c, r), (1, c, r), (2, c, r), world)
          # return sorted([(0, c, r), (1, c, r), (2, c, r)])

      if TicTacToeEnv._check_indices((0, c, 0), (1, c, 1), (2, c, 2), world):
        return TicTacToeEnv._check_indices((0, c, 0), (1, c, 1), (2, c, 2), world)
        # return sorted([(0, c, 0), (1, c, 1), (2, c, 2)])

      if TicTacToeEnv._check_indices((0, c, 2), (1, c, 1), (2, c, 0), world):
        return TicTacToeEnv._check_indices((0, c, 2), (1, c, 1), (2, c, 0), world)
        # return sorted([(0, c, 2), (1, c, 1), (2, c, 0)])
    
    # Diagonal 1
    if TicTacToeEnv._check_indices((0, 0, 0), (1, 1, 1), (2, 2, 2), world):
        return TicTacToeEnv._check_indices((0, 0, 0), (1, 1, 1), (2, 2, 2), world)
        # return sorted([(0, 0, 0), (1, 1, 1), (2, 2, 2)])

    # Diagonal 2
    if TicTacToeEnv._check_indices((0, 2, 0), (1, 1, 1), (2, 0, 2), world):
        return TicTacToeEnv._check_indices((0, 2, 0), (1, 1, 1), (2, 0, 2), world)
        # return sorted([(0, 2, 0), (1, 1, 1), (2, 0, 2)])

    # Diagonal 3
    if TicTacToeEnv._check_indices((0, 0, 2), (1, 1, 1), (2, 2, 0), world):
        return TicTacToeEnv._check_indices((0, 0, 2), (1, 1, 1), (2, 2, 0), world)
        # return sorted([(0, 0, 2), (1, 1, 1), (2, 2, 0)])

    # Diagonal 4
    if TicTacToeEnv._check_indices((0, 2, 2), (1, 1, 1), (2, 0, 0), world):
        return TicTacToeEnv._check_indices((0, 2, 2), (1, 1, 1), (2, 0, 0), world)
        # return sorted([(0, 2, 2), (1, 1, 1), (2, 0, 0)])
    
    return None

  def show_turn(self):
    return (self._round % TicTacToeEnv._PLAYERS_COUNT) + 1

  def show_result(self):
      msg = "Winner is '{}'!".format(self._result)
      print("==== Finished: {} ====".format(msg))
      return self._result
  
  def available_actions(self):
    available = []
    for i in range(3):
      for j in range(3):
        for k in range(3):
          if self._world[i][j][k] == 0:
            available.append("{}{}{}".format(i, j, k))
    return available