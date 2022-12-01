class PMOpt(object):
    @staticmethod
    def valid_xy(x, y):
        return 0 <= x and x < HT and 0 <= y and y < WD

    @staticmethod
    def neighbor(lid, radius):
        ret_neighbor = []
        x = lid // WD
        y = lid % WD
        for nx in range(max(0, x - radius), min(HT, x + radius + 1)):
            for ny in range(max(0, y - radius), min(WD, y + radius + 1)):
                nlid = nx * WD + ny
                if PM[lid][nlid] <= radius:
                    ret_neighbor.append(nlid)
        return ret_neighbor
