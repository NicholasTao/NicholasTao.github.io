from app.constant import XL, YL


class Battery(object):
    """battery info"""

    def __init__(self, lid, val):
        self.lid = lid
        self.val = val


class NodeInfo(object):
    """ map node info"""

    def __init__(self, score=0, robot=False, owner=-1, warranty_period=-1):
        self.is_way = True
        self.score = score
        self.is_robot = robot
        self.owner = owner
        self.warranty_period = warranty_period


class MapInfo(object):
    game_round = 0
    my_energy = 0
    all_btys = []

    def __init__(self, erg_limit, unit_erg, xy2sroce, occs):
        """ init map info

        :param erg_limit: The maximum energy amount that a player can accumulate.
        :param unit_erg: The unit energy for each camera.
        :param xy2sroce: The score of each land
        :param occs: All obstacles in the map
        """
        self.erg_limit = erg_limit
        self.unit_erg = unit_erg
        # land_scores y first
        self.node_info = [
            NodeInfo(xy2sroce[i][j])
            for j in range(XL)
            for i in range(YL)
        ]
        # todo wall score == 0 ???
        for occ_lid in occs:
            self.node_info[occ_lid].is_way = False

    def update_my_energy(self, all_energy):
        self.my_energy = all_energy

    def update_baterry(self, btys):
        """update battery info of whole map"""
        all_btys = []
        for bty in btys:
            bty_lid = bty.x * YL + bty.y
            self.node_info[bty_lid] = bty.amount
            all_btys.append(Battery(bty_lid, bty.amount))
        self.all_btys = all_btys

    def update_robots(self, robots):
        """update robots info of whole map"""
        for robot in robots:
            robot_lid = robot.x * YL + robot.y
            self.node_info[robot_lid].is_robot = True

    def update_occupied(self, occupied_lands):
        """update occupied_lands info"""
        for land in occupied_lands:
            land_lid = land.x * YL + land.y
            self.node_info[land_lid].owner = land.owner
            self.node_info[land_lid].warranty_period = land.warranty_period

    def update_by_action(self, robot, action):
        """update map info by robot's action"""
        # todo udpate robot location
        # todo update occupied
